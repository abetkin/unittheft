from unittest import TestLoader as _TestLoader
from .case import FunctionTestCase

class LoadTests:

    def __call__(self, _loader, suite, *args, **kw):
        loader = TestLoader()
        # loader.loadTestsFromModule(test_ex, 'test')


class TestLoader(_TestLoader):

    def loadTestsFromModule(self, module, *args, pattern=None, **kws):
        tests = []
        fun_type = type(lambda: None)
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, fun_type) and obj.__name__.startswith('test'):
                test = FunctionTestCase(obj)
                tests.append(test)
        return tests