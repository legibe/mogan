import json
import requests


"""
Only one error Exception, build like the HTTPError exception,
if has a member called code, holding the http error (int).
One is raise every time the status code returned by Zuora
is greater or equal to 300.
"""


class ZAPIError(Exception):

    def __init__(self, code, msg):
        super(ZAPIError, self).__init__(msg)
        self.code = code


"""
The API wrapper, to hide some details and provide a consistent logic
in handling exceptions. To build a session object (ZAPI) provide a 
config argument with the following compulsory fields:
{
    'header': {
        'content-type': defaults to 'application/json',
        'apiAccessKeyId': API user name,
        'apiSecretAccessKey': password,
    },
    'base_url': the right url for the type of tenant accessed
    # at the time of writing:
    # -- https://rest.apisandbox.zuora.com/v1 for sandboxes
    # -- https://rest.pt1.zuora.com/v1 for performance environments
    # -- https://api.zuora.com/rest/v1/ for production
}
"""


class ZAPI(object):

    def __init__(self, config, entity=None, **kwargs):
        self._entity = entity
        self._header = dict(config['header'], **kwargs)
        if 'content-type' not in config['header']:
            self._header['content-type'] = 'application/json'
        self._base = config['base_url'] + '/%s'
        
    def header(self):
        if self._entity is None:
            return dict(self._header)
        else:
            return dict(self._header, entityName=self._entity)

    def query(self, query_string):
        body = {'queryString': query_string}
        r = self.post(self._base % 'action/query', body=body)
        if r.status_code >= 300:
            raise ZAPIError(r.status_code, '%s - %s' % (r.reason, body['queryString']))
        return r.json()

    def query_more(self, query_result):
        if not query_result['done']:
            body = {'queryLocator': query_result['queryLocator']}
            r = self.post(self._base % 'action/queryMore', body=body)
            if r.status_code >= 300:
                raise ZAPIError(r.status_code, '%s - %s' % (r.reason, body['queryLocator']))
        return r.json()

    def get_object(self, identifier, class_, **fields):
        uri = '/%s/%s' % (class_, identifier)
        url = self._base % uri
        r = self.get(url, params=fields)
        if r.status_code >= 300:
            raise ZAPIError(r.status_code, '%s - GET Id: %s' % (r.reason, identifier))
        return r.json()

    def create_object(self, class_, **body):
        uri = '%s' % class_
        url = self._base % uri
        r = self.post(url, body=body)
        if r.status_code >= 300:
            raise ZAPIError(r.status_code, '%s - POST %s' % (r.reason, body))
        return r.json()

    def update_object(self, identifier, class_, **body):
        uri = '%s/%s' % (class_, identifier)
        url = self._base % uri
        r = self.put(url, body=body)
        if r.status_code >= 300:
            raise ZAPIError(r.status_code, '%s - PUT Id: %s' % (r.reason, identifier))

    def delete_object(self, identifier, class_):
        uri = '%s/%s' % (class_, identifier)
        url = self._base % uri
        r = self.delete(url)
        if r.status_code >= 300:
            raise ZAPIError(r.status_code, '%s - DELETE Id: %s' % (r.reason, identifier))
        return r.json()

    def describe_object(self, class_):
        uri = 'describe/%s' % class_
        url = self._base % uri
        r = self.get(url)
        if r.status_code >= 300:
            raise ZAPIError(r.status_code, '%s - DESCRIBE Id: %s' % (r.reason, class_))
        return r.text

    def post(self, url, body):
        return requests.post(url=url, headers=self.header(), data=json.dumps(body))

    def put(self, url, body):
        return requests.put(url=url, headers=self.header(), data=json.dumps(body))

    def get(self, url, params = None):
        return requests.get(url=url, headers=self.header(), params=params)

    def delete(self, url):
        return requests.delete(url=url, headers=self.header())

