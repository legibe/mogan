import unittest
from zuora.yaml_credentials import YAMLCredentials
from zuora.zapi import ZAPI, ZAPIError
from zuora.class_fields import ClassFields


class TestClassFields(unittest.TestCase):
    
    def setUp(self):
        self._session = session = ZAPI(YAMLCredentials('.creds', 'zuora', 'dev'))
    
    def test_get_fields(self):
        describe = ClassFields(self._session, 'Subscription')
        self.assertNotEqual(len(describe), 0)

    def test_get_fields_non_existing_class_raise(self):
        with self.assertRaises(ZAPIError):
            describe = ClassFields(self._session, 'NotAClass')

    def test_get_fields_non_existing_class_raise_code(self):
        try:
            describe = ClassFields(self._session, 'NotAClass')
        except ZAPIError as e:
            self.assertEqual(e.code, 500)
            

if __name__ == '__main__':
    unittest.main()

