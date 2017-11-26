import time


def exponential_wait(value):
    return value * 2


def linear_wait(value):
    return value + value


def constant_wait(value):
    return value


class WaitRetry(object):

    def __init__(self, attempts=3, initial_wait=0.2, wait_method=constant_wait):
        self._attempts = attempts
        self._number_of_attempts = attempts
        self._sleep = initial_wait
        self._method = wait_method

    def __call__(self):
        self._attempts -= 1
        if 0 < self._attempts < self._number_of_attempts:
            time.sleep(self._sleep)
            self._sleep = self._method(self._sleep)
        return self._attempts != 0

    def last_attempt(self):
        return self._attempts == 1

    @staticmethod
    def sleep(duration):
        time.sleep(duration)
