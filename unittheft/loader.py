from unittest import TestLoader as _TestLoader, TestSuite
from .case import FunctionTestCase

class LoadTests:

    def __init__(self, module_name):
        self.module_name = module_name


    def __call__(self, _loader, suite, *args, **kw):
        loader = TestLoader()
        tests = loader.loadTestsFromName(self.module_name)
        return TestSuite(tests)



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
