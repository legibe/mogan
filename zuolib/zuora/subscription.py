from zuora_object import ZuoraObject
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Subscription(ZuoraObject):

    class_name = 'Subscription'

    def __init__(self, session, identifier=None, name=None):
        if identifier is None:
            identifier = self.id_from_name(session, name)
        super(Subscription, self).__init__(session, identifier)

    def id_from_name(self, session, name):
        result = session.query("Select Id from %s where Name='%s'" % (self.class_name, name))
        if 'records' not in result or not len(result['records']):
            return None
        return result['records'][0]['Id']

    def account_id(self):
        if 'AccountId' in self:
            return self['AccountId']
        else:
            logger.info('subscription without account %s' % self)
        return None

    def invoice_id(self):
        if 'Id' not in self:
            return None
        result = self._session.query("Select InvoiceId from InvoiceItem where SubscriptionId='%s'" % (self['Id']))
        if 'records' not in result or not len(result['records']):
            # logger.info('cannot find Invoice %s' % self)
            return None
        return result['records'][0]['InvoiceId']

    def payment_id(self):
        pass
