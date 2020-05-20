from .case import threadlocal


def __getattr__(name):
    return getattr(threadlocal.case, name)

