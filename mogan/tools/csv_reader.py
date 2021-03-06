import csv
from collections import OrderedDict

class CSVReader(object):

    def __init__(self, filename, index_name=None, quotechar='"', encoding=None, delimiter=','):
        if encoding is None:
            encoding = self.get_encoding(filename, encoding)
        self._header = None
        self._row_count = 0
        self._index_name = index_name
        csv_file = open(filename, encoding=encoding, newline='')
        self._reader = csv.reader(csv_file, delimiter=delimiter, quotechar='"')

    def get_encoding(self, filename, encoding):
        with open(filename, 'rb') as f:
            prefix = list(f.read(2))
            if prefix[0] == 0xFF and prefix[1] == 0xFF:
                encoding = 'utf-8'
                # UTF-16 prefix is FFFE
            elif prefix[0] == 0xFF and prefix[1] == 0xFE:
                    encoding = 'utf-16'
            else:
                encoding = 'latin 1'
        return encoding

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
