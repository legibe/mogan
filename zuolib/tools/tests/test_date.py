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
        self.day_plus_5 = '2017-05-02'
        self.month_plus_5 = '2017-09'
        self.year_plus_5 = '2022'
        self.hour_plus_5 = '2017-04-27 22'
        self.minute_plus_5 = '2017-04-27 17:55'
        self.second_plus_5 = '2017-04-27 17:50:10'
        self.day_minus_5 = '2017-04-22'
        self.month_minus_5 = '2016-11'
        self.year_minus_5 = '2012'
        self.hour_minus_5 = '2017-04-27 12'
        self.minute_minus_5 = '2017-04-27 17:45'
        self.second_minus_5 = '2017-04-27 17:50:00'

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
            comparisons.append((getattr(self, field), getattr(date, '%s_int' % field)))
        for me, them in comparisons:
            self.assertEqual(me, them())
        
    # ------------------------------------------------------------
    # Date creation
    # ------------------------------------------------------------
    def test_create_system_date(self):
        try:
            d = Date()
        except Exception as e:
            self.fail('System date creation failed %s' % e)

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

    # ------------------------------------------------------------
    # Addition, subtraction
    # ------------------------------------------------------------
    def test_add_day(self):
        date = Day(self.build_date())
        new_date = date + 5
        self.assertEqual(str(new_date), self.day_plus_5)
        d = Day(date)
        d += 5
        self.assertEqual(str(d), self.day_plus_5)

    def test_add_month(self):
        date = Month(self.build_date())
        new_date = date + 5
        self.assertEqual(str(new_date), self.month_plus_5)
        d = Month(date)
        d += 5
        self.assertEqual(str(d), self.month_plus_5)

    def test_add_year(self):
        date = Year(self.build_date())
        new_date = date + 5
        self.assertEqual(str(new_date), self.year_plus_5)
        d = Year(date)
        d += 5
        self.assertEqual(str(d), self.year_plus_5)
    
    def test_add_hour(self):
        date = Hour(self.build_date())
        new_date = date + 5
        self.assertEqual(str(new_date), self.hour_plus_5)
        d = Hour(date)
        d += 5
        self.assertEqual(str(d), self.hour_plus_5)

    def test_add_minute(self):
        date = Minute(self.build_date())
        new_date = date + 5
        self.assertEqual(str(new_date), self.minute_plus_5)
        d = Minute(date)
        d += 5
        self.assertEqual(str(d), self.minute_plus_5)

    def test_add_second(self):
        date = Second(self.build_date())
        new_date = date + 5
        self.assertEqual(str(new_date), self.second_plus_5)
        d = Second(date)
        d += 5
        self.assertEqual(str(d), self.second_plus_5)

    def test_subtract_day(self):
        date = Day(self.build_date())
        new_date = date - 5
        self.assertEqual(str(new_date), self.day_minus_5)
        d = Day(date)
        d -= 5
        self.assertEqual(str(d), self.day_minus_5)

    def test_subtract_month(self):
        date = Month(self.build_date())
        new_date = date - 5
        self.assertEqual(str(new_date), self.month_minus_5)
        d = Month(date)
        d -= 5
        self.assertEqual(str(d), self.month_minus_5)

    def test_subtract_year(self):
        date = Year(self.build_date())
        new_date = date - 5
        self.assertEqual(str(new_date), self.year_minus_5)
        d = Year(date)
        d -= 5
        self.assertEqual(str(d), self.year_minus_5)
    
    def test_subtract_hour(self):
        date = Hour(self.build_date())
        new_date = date - 5
        self.assertEqual(str(new_date), self.hour_minus_5)
        d = Hour(date)
        d -= 5
        self.assertEqual(str(d), self.hour_minus_5)

    def test_subtract_minute(self):
        date = Minute(self.build_date())
        new_date = date - 5
        self.assertEqual(str(new_date), self.minute_minus_5)
        d = Minute(date)
        d -= 5
        self.assertEqual(str(d), self.minute_minus_5)

    def test_subtract_second(self):
        date = Second(self.build_date())
        new_date = date - 5
        self.assertEqual(str(new_date), self.second_minus_5)
        d = Second(date)
        d -= 5

    # ------------------------------------------------------------
    # Some special cases
    # ------------------------------------------------------------
    def test_leap_year(self):
        d = Day(Date('2012-02-28'))
        new_date = d + 5
        self.assertEqual(str(new_date), '2012-03-04')
        d = Day(Date('2012-03-03'))
        new_date = d - 63
        self.assertEqual(str(new_date), '2011-12-31')

    def test_non_leap_year(self):
        d = Day(Date('2013-02-28'))
        new_date = d + 5
        self.assertEqual(str(new_date), '2013-03-05')
        d = Day(Date('2013-03-03'))
        new_date = d - 63
        self.assertEqual(str(new_date), '2012-12-30')

    def test_change_of_year(self):
        d = Month('2014-11')
        d += 2
        self.assertEqual(d.year_int(), 2015)


if __name__ == '__main__':
    unittest.main()
