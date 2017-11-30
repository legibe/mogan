import unittest
from zuolib.tools.basic import time_in_seconds, big_number, big_number_short


class TestBasic(unittest.TestCase):

    # ------------------------------------------------------------
    # time_in_seconds. Split into different methods to help
    # locate the error quickly.
    # ------------------------------------------------------------
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

    # ------------------------------------------------------------
    # Big Number
    # ------------------------------------------------------------
    def test_big_number_thousand(self):
        self.assertEqual(big_number(3000), '3,000')

    def test_big_number_thousand_float(self):
        self.assertEqual(big_number(3000.12), '3,000.12')

    def test_big_number_million(self):
        self.assertEqual(big_number(1756342), '1,756,342')

    def test_big_number_million_float(self):
        self.assertEqual(big_number(1756342.25), '1,756,342.25')

    def test_big_number_billion(self):
        self.assertEqual(big_number(1756342498), '1,756,342,498')

    def test_big_number_billion_float(self):
        self.assertEqual(big_number(1756342498.999), '1,756,342,498.999')

    # ------------------------------------------------------------
    # Big Number Short
    # ------------------------------------------------------------
    def test_big_number_short_thousand(self):
        self.assertEqual(big_number_short(3000), '3K')

    def test_big_number_short_thousand_half(self):
        self.assertEqual(big_number_short(3500), '3.5K')
        
    def test_big_number_short_thousand_decimal(self):
        self.assertEqual(big_number_short(3542), '3.542K')

    def test_big_number_short_million(self):
        self.assertEqual(big_number_short(2000000), '2M')

    def test_big_number_short_million_half(self):
        self.assertEqual(big_number_short(2500000), '2.5M')
        
    def test_big_number_short_million_decimal(self):
        self.assertEqual(big_number_short(2546712), '2.546712M')

    def test_big_number_short_billion(self):
        self.assertEqual(big_number_short(2000000000), '2B')

    def test_big_number_short_billion_half(self):
        self.assertEqual(big_number_short(2500000000), '2.5B')
        
    def test_big_number_short_billion_decimal(self):
        self.assertEqual(big_number_short(2500436000), '2.500436B')
        

if __name__ == '__main__':
    unittest.main()
