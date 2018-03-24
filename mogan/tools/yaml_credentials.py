import os
import yaml


class YAMLCredentials(dict):

    def __init__(self, path, *args):
        if path[0] == '/':
            self._path = os.path.join(path, *args)
        else:
            self._path = os.path.join(os.path.expanduser('~'), path, *args) + '.yaml'
        with open(self._path) as f:
            config = yaml.load(f)
            super(YAMLCredentials, self).__init__(**config)
