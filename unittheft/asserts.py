from .case import threadlocal


# def __getattr__(name):
#     return getattr(threadlocal.case, name)


class AssertTrue:

    @property
    def __call__(self):
        return threadlocal.case.assertTrue

assertTrue = AssertTrue()