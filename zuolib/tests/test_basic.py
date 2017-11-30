import unittest
from zuolib.tools.basic import time_in_seconds


class TestBasic(unittest.TestCase):


    duration = [
        ('10s', 10),
        ('10 s', 10),
        ('55second', 55),
        ('55 second', 55),
        ('123seconds', 123),
        ('123 seconds', 123),
        ('3mn', 180),
        ('3 mn', 180),
        ('5m', 300),
        ('5 m', 300),
        ('35minute', 2100),
        ('35 minute', 2100),
        ('45minutes', 2700),
        ('45 minutes', 2700),
        ('2h', 7200),
        ('2 h', 7200),
        ('5hour', 18000),
        ('5 hour', 18000),
        ('12hours', 43200),
        ('12 hours', 43200),
        ('1d', 86400),
        ('1 d', 86400),
        ('3day', 259200),
        ('3 day', 259200),
        ('31days', 2678400),
        ('31 days', 2678400),
    ]

    def evaluate(self, index):
        self.assertEqual(self.duration[index][1],  time_in_seconds(self.duration[index][0]))

    def test_time_in_seconds0(self):
            self.evaluate(0)


    def test_time_in_seconds1(self):
            self.evaluate(1)


    def test_time_in_seconds2(self):
            self.evaluate(2)


    def test_time_in_seconds3(self):
            self.evaluate(3)


    def test_time_in_seconds4(self):
            self.evaluate(4)


    def test_time_in_seconds5(self):
            self.evaluate(5)


    def test_time_in_seconds6(self):
            self.evaluate(6)


    def test_time_in_seconds7(self):
            self.evaluate(7)


    def test_time_in_seconds8(self):
            self.evaluate(8)


    def test_time_in_seconds9(self):
            self.evaluate(9)


    def test_time_in_seconds10(self):
            self.evaluate(10)


    def test_time_in_seconds11(self):
            self.evaluate(11)


    def test_time_in_seconds12(self):
            self.evaluate(12)


    def test_time_in_seconds13(self):
            self.evaluate(13)


    def test_time_in_seconds14(self):
            self.evaluate(14)


    def test_time_in_seconds15(self):
            self.evaluate(15)


    def test_time_in_seconds16(self):
            self.evaluate(16)


    def test_time_in_seconds17(self):
            self.evaluate(17)


    def test_time_in_seconds18(self):
            self.evaluate(18)


    def test_time_in_seconds19(self):
            self.evaluate(19)


    def test_time_in_seconds20(self):
            self.evaluate(20)


    def test_time_in_seconds21(self):
            self.evaluate(21)


    def test_time_in_seconds22(self):
            self.evaluate(22)


    def test_time_in_seconds23(self):
            self.evaluate(23)


    def test_time_in_seconds24(self):
            self.evaluate(24)


    def test_time_in_seconds25(self):
            self.evaluate(25)



if __name__ == '__main__':
    unittest.main()
