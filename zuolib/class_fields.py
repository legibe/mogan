import xml.etree.ElementTree as ET

"""
Represents a set of all fields defined in a Zuora class, including custom fields.
Arguments:
    session: an instance of ZAPI
    class_name: the name of the Zuora class, e.g. Subscription, Product etc...
    
Example:
session = ZAPI(config)
describe = ClassFields(session, 'Subscription)
for x in sorted(describe):
    print(x)
"""


class ClassFields(set):

    def __init__(self, session, class_name):
        super(ClassFields, self).__init__()
        description = session.describe_object(class_name)
        root = ET.fromstring(description)
        for x in root.findall('./fields/field/name'):
            self.add(x.text)
