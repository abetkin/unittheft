import threading
from unittest import TestCase as _TestCase
from unittest.util import strclass


threadlocal = threading.local()
threadlocal.case: _TestCase


class TestCase(_TestCase):

    def __call__(self, result):
        threadlocal.case = self
        try:
            super().__call__(result)
        finally:
            threadlocal.case = None


class FunctionTestCase(TestCase):

    def __init__(self, test_func):
        self.test_func = test_func
        setattr(self, self._testMethodName, self.test_func)

    def doCleanups(self):
        pass

    _testMethodDoc = None

    @property
    def _testMethodName(self):
        return self.test_func.__name__

    def __str__(self):
        f = self.test_func
        return f"{f.__module__}.{f.__name__}"


    def __repr__(self):
        return f'<FunctionTestCase: {self}'