import time
import unittest
import thread
import threading

from timeout import timeout


class TestTimeout(unittest.TestCase):
    def test_setting_none_timeout_works(self):

        expected = range(1, 101)
        result = []

        @timeout(None)
        def fn():
            i = 0
            while i < 100:
                i += 1
                result.append(i)

        fn()
        self.assertEqual(expected, result)

    def test_happy_path(self):
        expected = 3

        global result
        result = 0

        @timeout(3)
        def fn():
            global result
            while True:
                result += 1
                time.sleep(1)

        fn()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()


