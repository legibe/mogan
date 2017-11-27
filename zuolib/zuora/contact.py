from zuora_object import ZuoraObject


"""
Contact class and some helper methods
"""


class Contact(ZuoraObject):

    def account_id(self):
        return self['AccountId']

