# --------------------------------------------------------------------------------
# Author: Claude Gibert
#
# --------------------------------------------------------------------------------
import json

from .schemareader import SchemaReader


class JSONReader(object):

    @staticmethod
    def read(filename):
        with open(filename) as f:
            try:
                schema = json.load(f)
            except Exception as e:
                print(filename, e)
                raise
            if not isinstance(schema, list):
                schema = [schema]
            return schema


SchemaReader.register('json', JSONReader)
