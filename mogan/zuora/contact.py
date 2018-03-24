from .zuora_object import ZuoraObject


"""
Contact class and some helper methods
"""


class Contact(ZuoraObject):

    _class_name = 'Contact'

    def account_id(self):
        return self['AccountId']

