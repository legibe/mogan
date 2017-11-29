import unittest
import time
from zuolib.tools.factory import create_factory


class TestFactory(unittest.TestCase):

    @staticmethod
    def class_1():
        def internal():
            return '1'
        return internal

    @staticmethod
    def class_2():
        def internal():
            return '2'
        return internal

    @staticmethod
    def class_default():
        def internal():
            return 'default'
        return internal

    def test_create_factory(self):
        factory = create_factory('Testing1')
        try:
            from zuolib.tools.factory import Testing1Factory
        except ModuleNotFoundError:
            self.fail('factory was not added to the module')

    def test_register_factory_with_default(self):
        factory = create_factory('Testing2')
        factory.register('class1', self.class_1)
        factory.register('class2', self.class_2)
        factory.register_default(self.class_default)

        action = factory.create('class1')
        self.assertEqual(action(), '1')
        action = factory.create('class2')
        self.assertEqual(action(), '2')
        action = factory.create('unknown')
        self.assertEqual(action(), 'default')

    def test_register_factory_without_default(self):
        factory = create_factory('Testing3')
        factory.register('class1', self.class_1)
        factory.register('class2', self.class_2)

        action = factory.create('class1')
        self.assertEqual(action(), '1')
        action = factory.create('class2')
        self.assertEqual(action(), '2')
        with self.assertRaises(IndexError):
            action = factory.create('unknown')

    def test_is_registered(self):
        factory = create_factory('Testing2')
        factory.register('class1', self.class_1)
        factory.register('class2', self.class_2)
        factory.register_default(self.class_default)

        self.assertTrue(factory.is_registered('class1'))
        self.assertFalse(factory.is_registered('unknown'))

    def test_registered_list(self):
        factory = create_factory('Testing2')
        factory.register('class1', self.class_1)
        factory.register('class2', self.class_2)
        factory.register_default(self.class_default)

        self.assertEqual(factory.registered(), {'class1', 'class2'})

if __name__ == '__main__':
    unittest.main()
