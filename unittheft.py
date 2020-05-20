import threading
from functools import wraps

from unittest import TestCase


threadlocal = threading.local()
threadlocal.case: TestCase

@wraps(TestCase.assertTrue)
def assertTrue(*args, **kw):
    threadlocal.case.assertTrue(*args, **kw)


