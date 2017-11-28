import unittest
from tools.date import Date, Day, Month, Year, Hour, Minute, Second


class TestDate(unittest.TestCase):
    
    def setUp(self):
        self.day = 27
        self.month = 4
        self.year = 2017
        self.hour = 17
        self.minute = 50
        self.second = 5

    def build_date(self):
        return '%d-%02d-%02d %02d:%02d:%02d' % (
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second)

    def compare_dates(self, date, *fields):
        comparisons = []
        for field in fields:
            comparisons.append((getattr(self, field), getattr(date, field)))
        for me, them in comparisons:
            self.assertEqual(me, int(them()))
        
    # ------------------------------------------------------------
    # Date creation
    # ------------------------------------------------------------
    def test_create_system_date(self):
        try:
            d = Date()
        except Exception as e:
            self.fail('System date creation failed %' % e)

    def test_create__date_int(self):
        try:
            d = Date(20170427)
        except Exception as e:
            self.fail('Int date creation failed %s' % e)

    def test_create__date_str(self):
        try:
            d = Date('20170427')
        except Exception as e:
            self.fail('Str date creation failed %s' % e)

    def test_create__date_str_formatted(self):
        try:
            d = Date('2017-04-27')
        except Exception as e:
            self.fail('Str formatted date creation failed %s' % e)

    def test_create__date_from_date(self):
        date = Date('2017-04-27')
        try:
            d = Date(date)
        except Exception as e:
            self.fail('date creation from date failed %s' % e)

    def test_create__date_from_datetime(self):
        date = Date('2017-04-27')
        try:
            d = Date(date.datetime())
        except Exception as e:
            self.fail('date creation from datetime failed %s' % e)

    # ------------------------------------------------------------
    # Day creation
    # ------------------------------------------------------------
    def test_create__day_from_date(self):
        date = self.build_date()
        try:
            d = Day(date)
        except Exception as e:
            self.fail('day creation from date failed %s' % e)
        self.compare_dates(d, 'year', 'month', 'day')

    # ------------------------------------------------------------
    # Month creation
    # ------------------------------------------------------------
    def test_create__month__from_date(self):
        date = Date('2017-04-27')
        try:
            d = Month(date)
        except Exception as e:
            self.fail('month creation from date failed %s' % e)
        self.compare_dates(d, 'year', 'month')

    # ------------------------------------------------------------
    # Year creation
    # ------------------------------------------------------------
    def test_create__year__from_date(self):
        date = Date('2017-04-27')
        try:
            d = Month(date)
        except Exception as e:
            self.fail('year creation from date failed %s' % e)
        self.compare_dates(d, 'year')

    # ------------------------------------------------------------
    # Hour creation
    # ------------------------------------------------------------
    def test_create__hour_from_date(self):
        date = self.build_date()
        try:
            d = Hour(date)
        except Exception as e:
            self.fail('hour creation from date failed %s' % e)
        self.compare_dates(d, 'year', 'month', 'day', 'hour')

    # ------------------------------------------------------------
    # Minute creation
    # ------------------------------------------------------------
    def test_create__minute_from_date(self):
        date = self.build_date()
        try:
            d = Minute(date)
        except Exception as e:
            self.fail('minute creation from date failed %s' % e)
        self.compare_dates(d, 'year', 'month', 'day', 'hour', 'minute')

    # ------------------------------------------------------------
    # Second creation
    # ------------------------------------------------------------
    def test_create__second_from_date(self):
        date = self.build_date()
        try:
            d = Second(date)
        except Exception as e:
            self.fail('second creation from date failed %s' % e)
        self.compare_dates(d, 'year', 'month', 'day', 'hour', 'minute', 'second')

if __name__ == '__main__':
    unittest.main()

