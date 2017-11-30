import unittest
from zuolib.tools.basic import time_in_seconds


class TestBasic(unittest.TestCase):


    def test_dummy(self):
        self.assertTrue(True)


durations = {
        '10s': 10,
        '10 s': 10,
        '55second': 55,
        '55 second': 55,
        '123seconds': 123,
        '123 seconds': 123,
        '3mn': 180,
        '3 mn': 180,
        '5m': 300,
        '5 m': 300,
        '35minute': 2100,
        '35 minute': 2100,
        '45minutes': 2700,
        '45 minutes': 2700,
        '2h': 7200,
        '2 h': 7200,
        '5hour': 18000,
        '5 hour': 18000,
        '12hours': 43200,
        '12 hours': 43200,
        '1d': 86400,
        '1 d': 86400,
        '3day': 259200,
        '3 day': 259200,
        '0.5days': 43200,
        '0.5 days': 43200,
    }


class RunTest(object):
    def __init__(self, label, value):
        self._label = label
        self._value = value

    def __call__(self):
        TestBasic.assertEqual(self._value, time_in_seconds(self._label))

for label, value in durations.items():
    print(label)
    setattr(TestBasic, 'test_%s' % label.replace(' ','_'), RunTest(label, value))
print(dir(TestBasic))

if __name__ == '__main__':
    unittest.main()
