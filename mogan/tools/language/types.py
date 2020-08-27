# --------------------------------------------------------------------------------
# Author: Claude Gibert
#
# --------------------------------------------------------------------------------
import re
import sys
import builtins
from ..factory import create_factory
from ..date import Second, Day
from ..basic import big_number


factory = create_factory('TypeCreation')


class Types(factory):

    @classmethod
    def create(cls, name, *args, **kwargs):
        try:
            result = super(Types, cls).create(name, *args, **kwargs)
        except IndexError:
            result = getattr(builtins, name)(*args, **kwargs)
        return result


class Price(float):
    def __new__(cls, value):
        if isinstance(value, str):
            value = float(re.sub(',', '', value))
        return float.__new__(value)

    def __str__(self):
        s = super(Price, self).__str__()
        return big_number(s)


class Volume(int):
    def __new__(cls, value):
        if isinstance(value, str):
            value = int(re.sub(',', '', value))
        return int.__new__(value)

    def __str__(self):
        s = super(Volume, self).__str__()
        return big_number(s)


class DateTime(object):
    def __new__(cls, value):
        # will issue an exception if the date is not valid
        v = Second(value).string_value()
        return str.__new__(v)


class FormattedDateTime(object):
    def __new__(cls, value):
        # will issue an exception if the date is not valid
        v = Second(value)
        return str.__new__(str, v)

        
class FormattedDateNoTime(object):
    def __new__(cls, value):
        # will issue an exception if the date is not valid
        v = Day(value)
        return str.__new__(str, v)


class PyDateTime(object):
    def __new__(cls, value):
        # will issue an exception if the date is not valid
        v = Second(value)
        return v.datetime()

class PyDate(object):
    def __new__(cls, value):
        # will issue an exception if the date is not valid
        return Day(value)

class Boolean(object):
    def __new__(cls, value):
        result = False
        if isinstance(value, str):
            value = value.lower()
            if value == 'yes' or value == 'y':
                result = True
        elif isinstance(value, bool):
            result = value
        elif isinstance(value, int):
            result = value != 0
        return result


Types.register('price', Price)
Types.register('volume', Volume)
Types.register('datetime', DateTime)
Types.register('py_date', PyDate)
Types.register('formatted_datetime', FormattedDateTime)
Types.register('formatted_day', FormattedDateNoTime)
Types.register('py_datetime', PyDateTime)
Types.register('boolean', Boolean)
