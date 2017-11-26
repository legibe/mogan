from multiprocessing import Process
from queue import Empty


class Worker(Process):

    max_retries = 4
    timeout = 120 # seconds

    def __init__(self, queue, processor, expected=None):
        Process.__init__(self)
        self._queue = queue
        self._processor = processor
        self._expected = expected

    def run(self):
        if self._expected is None:
            self.run_unexpected()
        else:
            self.run_expected()

    def run_unexpected(self):
        retries = 0
        while True:
            try:
                entry = self._queue.get(timeout=self.timeout)
                self._queue.task_done()
                self._processor(entry)
            except Empty:
                print('empty')
                retries += 1
                if retries >= self.max_retries:
                    return
            else:
                retries = 0

    def run_expected(self):
        count = 0
        while True:
            try:
                entry = self._queue.get(timeout=0.5)
                self._queue.task_done()
                self._processor(entry)
            except Empty:
                if count == self._expected:
                    return
            else:
                count += 1
