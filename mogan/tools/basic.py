# --------------------------------------------------------------------------------
# Author: Claude Gibert
#
# --------------------------------------------------------------------------------
import re
from collections import Sequence


def is_list(a):
    return type(a) == list or type(a) == tuple


def to_list(a):
    if not is_list(a):
        a = [a]
    return a


def no_list(a):
    if is_list(a):
        a = a[0]
    return a


def time_in_seconds(s):
    """
    :param s: a string, for example 12, 12mn, 4h, 4hours, 2 days etc...
    :return: the time in seconds
    """
    factors = {
        's': 1,
        'second': 1,
        'seconds': 1,
        'mn': 60,
        'm': 60,
        'minute': 60,
        'minutes': 60,
        'h': 3600,
        'hour': 3600,
        'hours': 3600,
        'd': 86400,
        'day': 86400,
        'days': 86400,
    }

    s = str(s).lower().strip()
    negative = False
    if s[0] == '-':
        negative = True
        s = s[1:]
    unit = re.findall('[a-z]+$', s)
    number = int(re.findall('^[0-9]+', s)[0])
    factor = 1
    if len(unit) > 0:
        if not unit[0] in factors:
            raise ValueError('In time %s, unknow unit: %s' % (s, unit[0]))
        factor = factors[unit[0]]
        if negative:
            factor = -factor
    return number * factor


def big_number(value):
    """
        Formats a number to add comas for multiples of 1,000
    """
    s = str(value)
    parts = s.split('.')
    whole = parts[0]
    dec = ''
    if len(parts) > 1:
        dec = parts[1]
    new = ''
    ll = len(whole)
    for i in range(ll):
        index = ll - i - 1
        new += whole[i]
        if index % 3 == 0 and index != 0:
            new += ','
    if len(dec) > 0:
        new += '.' + dec
    return new


def big_number_short(value):
    """
        Shortens a number to the nearest facto (K, M, B)
    """
    abbreviations = ['', 'K', 'M', 'B']

    value = float(value)
    i = 0
    while value >= 1000 and i < len(abbreviations):
        i += 1
        value /= 1000
    v = str(value)
    v = v.replace('.0', '')
    return v + abbreviations[i]


def substitute_string_from_dict(a, variables):
    """Substitutes variables of the form ${varname} with
    values provided in a dictionary
    """
    if isinstance(a, str):
        variable_names = re.findall('\${(.*?)}', a)
        for var in variable_names:
            if var in variables:
                a = re.sub('\${%s}' % var, variables[var], a)
    return a


def substitute_structure_from_dict(a, variables):
    if isinstance(a, dict):
        for key, item in a.items():
            a[key] = substitute_structure_from_dict(item, variables)
    elif isinstance(a, list):
        for i, item in enumerate(a):
            a[i] = substitute_structure_from_dict(item, variables)
    else:
        a = substitute_string_from_dict(a, variables)
    return a

def is_sequence_and_not_string(a):
    return isinstance(a,Sequence) and not isinstance(a, str)

def no_list(a): 
    if is_list(a):
        a = a[0]
    return a

def make_list(a):
    if not is_list(a):
        a = [a]
    return a

