import csv

class CSVWriter(object):

    quoting = {
        'all': csv.QUOTE_ALL,
        'minimal': csv.QUOTE_MINIMAL,
        'non-numeric': csv.QUOTE_NONNUMERIC,
        'none': csv.QUOTE_NONE,
    }
    mode = {
        'new': 'w',
        'append': 'a'
    }

    def __init__(self, filename, encoding='utf-8', delimiter=',', quotechar='"', quoting='minimal', newline='', mode='new'):
        f = open(filename, self.mode[mode], encoding=encoding, newline=newline)
        self._writer = csv.writer(f, delimiter=delimiter, quotechar=quotechar, quoting=self.quoting[quoting])

    def write_row(self, data):
        self._writer.writerow(data)
