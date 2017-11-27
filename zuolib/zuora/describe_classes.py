import json
import xml.etree.ElementTree as ET
from zapi import ZAPI


classes = [
    'Subscription',
    'Account',
    'Contact',
    'Invoice',
    'Payment',
    'PaymentMethod'
]

result = {}
for klass in classes:
    api = ZAPI(entity='EMEA', env='dev')
    description = api.describeObject(klass)
    root = ET.fromstring(description)
    fields = { x.text:True for x in root.findall('./fields/field/name') }
    result[klass.lower()] = fields
    with open('classes.json', 'w') as f:
        json.dump(result, f, indent=4)
