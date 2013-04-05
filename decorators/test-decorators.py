import unittest


def my_decorator(fn):
    print('-before decorate')

    def decorate(*args, **kwargs):
        print('-before function')
        result = fn(*args, **kwargs)
        print('-after function')
        return result

    print('-after decorate')
    return decorate


@my_decorator
def my_function():
    return 5


class TestDecorators(unittest.TestCase):

    def test_when_does_it_wrap_with_args(self):
        value = my_function()

        self.assertEqual(5, value)

        self.assertTrue(False)
