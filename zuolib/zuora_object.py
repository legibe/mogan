

class ZuoraObject(dict):

    class_name = None

    def __init__(self, session, identifier):
        super(ZuoraObject, self).__init__()
        if self.class_name is None:
            raise IndexError('Unknown class')
        self._session = session
        if identifier is not None:
            result = self._session.get_object(identifier, 'object/%s' % self.class_name)
            for k, i in result.items():
                self[k] = i

    def id(self):
        if 'Id' in self:
            return self['Id']
        return None
