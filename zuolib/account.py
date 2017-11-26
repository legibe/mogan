from zuora_object import ZuoraObject
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Account(ZuoraObject):

    class_name = 'Account'

    def __init__(self, session, identifier=None, crm_id=None):
        if identifier is None:
            identifier = self.id_from_crm_id(session, crm_id)
            print(identifier)
        super(Account, self).__init__(session, identifier)

    def id_from_crm_id(self, session, crm_id):
        result = session.query("Select Id from %s where crmid like '%s%%'" % (self.class_name, crm_id))
        if 'record' not in result or not len(result['records']):
            logger.info('cannot find CrmId %s' % crm_id)
            return None
        return result['records'][0]['Id']

    def bill_to_id(self):
        if 'BillToId' in self:
            return self['BillToId']
        else:
            logger.info('No BillToId in %s' % self)
        return None

    def sold_to_id(self):
        if 'SoldToId' in self:
            return self['SoldToId']
        else:
            logger.info('No SoldToId in %s' % self)
        return None

    def payment_method_id(self):
        if 'DefaultPaymentMethodId' not in self:
            return None
        return self['DefaultPaymentMethodId']

    def payment_id(self):
        result = self._session.query("select Id from Payment where AccountId='%s'" % self.id())
        if 'record' not in result or not len(result['records']):
            return None
        if len(result['records']) > 1:
            raise IndexError('more than one payment returned')
        return result['records'][0]['Id']

    def subscription_ids(self):
        result = []
        if 'Id' in self:
            result = self._session.query("Select Id from Subscription where AccountId='%s'" % (self['Id']))
            if 'records' in result and len(result['records']):
                result = [x['Id'] for x in result['records']]
        return result
