import unittest
import time
from zuolib.tools.timer import Timer


class TestTimer(unittest.TestCase):

    def test_timing(self):
        delay = 0.8
        with Timer() as t:
            time.sleep(delay)
            self.assertLessEqual(t.snapshot() - delay, 0.1)
            time.sleep(delay)
        self.assertLessEqual(t() - 2*delay, 0.1)

if __name__ == '__main__':
    unittest.main()
