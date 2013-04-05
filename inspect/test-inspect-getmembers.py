import unittest
import inspect


class InnerClass(object):

    def get_inner_stuff(self):
        return 'inner stuff'


class SimpleClass(object):

    def __unicode__(self):
        return u'SimpleClass'

    def get_stuff(self):
        return 'my super stuff'

    inner = InnerClass()


class TestInspect(unittest.TestCase):

    def test_getmembers(self):
        sc = SimpleClass()

        members = inspect.getmembers(SimpleClass)
        methods = [member[0] for member in members]
        member_dict = {}
        for name, item in members:
            member_dict[name] = item

        self.assertTrue('__unicode__' in methods)
        self.assertTrue('get_stuff' in methods)
        self.assertTrue('inner' in methods)

        self.assertFalse(inspect.ismodule(sc))
        self.assertFalse(inspect.ismodule(SimpleClass))

        self.assertFalse(inspect.isclass(sc))
        self.assertTrue(inspect.isclass(SimpleClass))

        get_stuff = member_dict['get_stuff']
        self.assertFalse(inspect.isfunction(get_stuff))
        self.assertTrue(inspect.ismethod(get_stuff))

        self.assertFalse(inspect.ismethod(member_dict['inner']))
