import unittest
import inspect


def my_func(x, y=5, z=8):
    print x, y, z


class TestArgSpec(unittest.TestCase):

    def test_getargspec(self):
        args, vargs, varkw, defaults = inspect.getargspec(my_func)

        print args
        print vargs
        print varkw
        print defaults

        kwargs = args[len(defaults) - 1:]

        self.assertEqual('y', kwargs[0])
        self.assertEqual('z', kwargs[1])

        self.assertEqual(5, defaults[0])
        self.assertEqual(8, defaults[1])
