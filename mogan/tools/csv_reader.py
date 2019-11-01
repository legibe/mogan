import csv
from collections import OrderedDict

class CSVReader(object):

    def __init__(self, filename, index_name=None, quotechar='"', encoding='utf-8', delimiter=','):
        self._header = None
        self._row_count = 0
        self._index_name = index_name
        csv_file = open(filename, encoding=encoding, newline='')
        self._reader = csv.reader(csv_file, delimiter=delimiter, quotechar='"')

    def __call__(self):
            index = 0
            increment = 0
            for row in self._reader:
                if self._header is None:
                    self._header = [x.strip() for x in row]
                else:
                    self._row_count += 1
                    record = {}
                    for i, value in enumerate(row):
                        record[self._header[i]] = value
                    if self._index_name is None:
                        increment += 1
                        index = increment
                    else:
                        index = record[self._index_name]
                    yield(record)

    @property
    def header(self):
        return self._header

    @property
    def index_name(self):
        return self._index_name

    @property
    def row_count(self):
        return self._row_count
