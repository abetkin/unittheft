from functools import wraps

from unittheft.case import threadlocal, TestCase


@wraps(TestCase.assertTrue)
def assertTrue(*args, **kw):
    threadlocal.case.assertTrue(*args, **kw)


