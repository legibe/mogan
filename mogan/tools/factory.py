# --------------------------------------------------------------------------------
# Author: Claude Gibert
#
# --------------------------------------------------------------------------------
import sys

"""
A factory to hold classes under registered strings. Factory classes are generated
automatically by the function createFactory. New classes are also added to the
module's namespace so they become visible by importers.
createFactory('Object') creates the class called ObjectFactory
"""


class Factory(object):

    @classmethod
    def register(cls, name, what):
        cls._members[name] = what

    # if set, any unknown name will create one of those
    @classmethod
    def register_default(cls,what):
        cls._default = what

    @classmethod
    def create(cls,name,*args,**kwargs):
        if name not in cls._members:
            if cls._default is not None:
                return cls._default(*args, **kwargs)
            else:
                raise IndexError('%s "%s" is unknown, available: %s' % (cls._name,name,', '.join(cls._members.keys())))
        return cls._members[name](*args,**kwargs)

    @classmethod
    def registered(cls):
        return set(cls._members.keys())

    @classmethod
    def is_registered(cls,name):
        return name in cls._members


def create_factory(name):
    me = sys.modules[__name__]
    name = '%sFactory' % name
    if not hasattr(me,name):
        setattr(sys.modules[__name__], name, type(name, (Factory,), {'_name': name, '_members': {}, '_default': None}))
    return getattr(me,name)
