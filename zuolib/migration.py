import json
import os
import logging
from multiprocessing import JoinableQueue
from worker import Worker
from zapi import ZAPI
from object_loader import ObjectLoader


FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


class Processor(object):

    def __init__(self, queue, session):
        self._data = queue
        self._session = session

    def __call__(self, entry):
        data = ObjectLoader.load_from_subscription_id(self._session, entry)
        self._data.put(data)


class Writer(object):

    def __init__(self):
        self._errors = open('subscriptions/rubbish.txt', 'a+')
        self._files = {}

    def get_file(self, country):
        if country not in self._files:
            filename = country.replace(' ', '_')
            filename = filename.lower()
            f = open('subscriptions/%s.txt' % filename, 'a+')
            self._files[country] = f
        return self._files[country]

    def __call__(self, entry):
        stream = self._errors
        if 'delivery' in entry:
            if 'Country' in entry['delivery']:
                stream = self.get_file(entry['delivery']['Country'])
        entry = json.dumps(entry)
        stream.write('%s\n' % entry)
        stream.flush()


def check_workers(worker_list):
    new_list = []
    for w in worker_list:
        if not w.is_alive() and w.exitcode == 17:
            logger.info('restarting a worker')
            w = Worker(source, Processor(sink, ZAPI(env='migration', entity=entity)))
            w.start()
        new_list.append(w)
    return new_list


def directory_list(path, extension=None):
    result = []
    if os.path.exists(path):
        files = os.listdir(path)
        if extension is None:
            result = files
        else:
            for file in files:
                l = file.split('.')
                if l[-1] == extension:
                    result.append(file)
    return result


def load_existing_subscriptions(subset):
    file_list = directory_list('subscriptions', 'txt')
    for filename in file_list:
        with open('subscriptions/%s' % filename) as f:
            line = f.readline().strip()
            while line:
                entry = json.loads(line)
                subset.add(entry['subscription']['Id'])
                line = f.readline().strip()
    return subset


entity = 'AM'
subscription_done = load_existing_subscriptions(set())
print(len(subscription_done))
sink = JoinableQueue()
source = JoinableQueue()
funnel = Worker(sink, Writer())
funnel.start()
workers = []
for i in range(50):
    worker = Worker(source, Processor(sink, ZAPI(env='migration', entity=entity)))
    workers.append(worker)
    worker.start()

api = ZAPI(env='migration', entity=entity)
result = api.query("select Id from Subscription where Version='1'")
while result:
    for i, record in enumerate(result['records']):
        if record['Id'] not in subscription_done:
            source.put(record['Id'])
    workers = check_workers(workers)
    result = api.query_more(result)
source.join()
