from .zuora_object import ZuoraObject


class Invoice(ZuoraObject):

    def __init__(self, *args, **kwargs):
        super(Invoice, self).__init__(*args, **kwargs)
        # blank the body which the pdf of the invoice
        self['Body'] = ''
