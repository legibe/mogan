"""
The root class for classes representing an equivalent class in Zuora.
It implemented CRUD operations with a double meaning creator:
- read from Id
- create from data
To create an instance of the class:
- ZuoraObject('12345678') reads an object with Id='12345678'
- ZuoraObject(field1=a, field2=b, field3=c, etc...) attempts
  create an object initialised with the field values.
"""


class ZuoraObject(dict):

    """
        give us a change of override when the actual class name
        cannot be used for the equivalent class in the library
        default behaviour: use the current class name.
    """
    class_name = None

    def __init__(self, session, identifier, **kwargs):
        super(ZuoraObject, self).__init__()
        if self.class_name is None:
            self.class_name = self.__class__.__name__
        self._session = session
        if identifier is None:
            self.create(**kwargs)
        else:
            self.read(identifier)

    def id(self):
        if 'Id' in self:
            return self['Id']
        return None

    def create(self, **kwargs):
        self._session.create_object(self.class_name, **kwargs)
        # the previous raises an exception if something went wrong
        # so the following code is not executed in that case, that
        # the object keeps empty.
        for k, i in kwargs.items():
            self[k] = i

    def read(self, identifier):
        result = self._session.get_object(identifier, 'object/%s' % self.class_name)
        # the previous raises an exception if something went wrong
        # so the following code is not executed in that case, that
        # the object keeps empty.
        for k, i in result.items():
            self[k] = i

    def update(self, **kwargs):
        result = self._session.update_object(self.id(), **kwargs)
        # the previous raises an exception if something went wrong
        # so the following code is not executed in that case, that
        # the object keeps empty.
        for k, i in result.items():
            self[k] = i

    def delete(self):
        self._session.update_object(self.id())
        # when deleted, we want an empty object
        self.clear()

