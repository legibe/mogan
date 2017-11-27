from zuora_object import ZuoraObject


"""
The Account class with some helper method. Please note that you can build 
an account object from a cmd_id or an account_number.
"""


class Account(ZuoraObject):

    @classmethod
    def account_from_crm_id(cls, session, crm_id):
        result = session.query("Select Id from %s where crmid like '%s%%'" % (cls.class_name, crm_id))
        return result['records'][0]['Id']

    @classmethod
    def account_from_account_number(cls, session, account_number):
        result = session.query("Select Id from %s where AccountNumber='%s%%'" % (cls.class_name, account_number))
        return result['records'][0]['Id']

    def bill_to_id(self):
        if 'BillToId' in self:
            return self['BillToId']
        return None

    def sold_to_id(self):
        if 'SoldToId' in self:
            return self['SoldToId']
        return None

    def default_payment_method_id(self):
        if 'DefaultPaymentMethodId' in self:
            return self['DefaultPaymentMethodId']
        return None

    def payment_ids(self):
        result = self._session.query("select Id from Payment where AccountId='%s'" % self.id())
        if 'record' not in result or not len(result['records']):
            return []
        result = [x['Id'] for x in result['records']]
        return result

    def subscription_ids(self):
        result = self._session.query("Select Id from Subscription where AccountId='%s'" % (self['Id']))
        if 'records' in result and len(result['records']):
            result = [x['Id'] for x in result['records']]
        return result
