# --------------------------------------------------------------------------------
# Author: Claude Gibert
#
# --------------------------------------------------------------------------------
from ..factory import create_factory
from .schema_validate import SchemaValidate

SchemaReaderFactory = create_factory('SchemaReader')


class SchemaReader(SchemaReaderFactory):
    cache = {}

    @classmethod
    def read(cls, name, fullpath, extension='json'):
        if name in cls.cache:
            return cls.cache[name]

        filename = '%s.%s' % (name, extension)
        reader = SchemaReaderFactory.create(extension)
        # we take the first one, if more than one was found, we assume that
        # the first one is the one to use
        schema = reader.read(paths[0])
        for s in schema:
            cls.cache[s['schema']] = s
            SchemaValidate.validate(s)
        return cls.cache[name]
