# --------------------------------------------------------------------------------
# Author: Claude Gibert
#
# --------------------------------------------------------------------------------
from ..factory import create_factory
from ..basic import to_list
from ..basic import time_in_seconds

ValidationFactory = create_factory('Validation')


class Validate(ValidationFactory):
    pass


class ValidateSetChoice(object):
    def __init__(self, *args):
        self._values = set(args)

    def __call__(self, schemas, keyword, value, request):
        values = to_list(value)
        for v in values:
            if v not in self._values:
                raise IndexError('For keyword "%s", value "%s" is not valid, available choices: %s' % (
                    keyword, v, ', '.join(self._values)))
        return value


class ValidateExclude(object):
    def __init__(self, *args):
        self._values = list(args)

    def __call__(self, schemas, keyword, value, request):
        count = 0
        keywords = self._values + [keyword]
        for value in keywords:
            if value in request and request[value] is not None:
                count += 1
        if count != 1:
            raise ValueError('Keywords %s are exclusive, at least one and only one of them should be defined' % (
                ', '.join(keywords)))
        for k in keywords:
            if k in request and request[k] is None:
                del (request[k])
        return value


class MinimumTime(object):
    def __init__(self, *args):
        self._min = time_in_seconds(args[0])

    def __call__(self, schemas, keyword, value, request):
        value = time_in_seconds(value)
        if value < self._min:
            raise ValueError('The keyword "%s" (%s) should be at least %d seconds' % (keyword, value, self._min))
        return value


class TimeWithUnit(object):
    def __call__(self, schemas, keyword, value, request):
        return time_in_seconds(value)


Validate.register('set-choices', ValidateSetChoice)
Validate.register('validate-exclude', ValidateExclude)
Validate.register('minimum-time', MinimumTime)
Validate.register('time-with-unit', TimeWithUnit)

