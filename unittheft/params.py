import inspect
import sys


class MyExc(Exception):
    pass

class MyExc(Exception):
    def __init__(self, locals):
        self.locals = locals


class Params:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        fr = inspect.currentframe()
        raise MyExc(fr.f_back.f_locals)


params = Params()

def test():
    with params:
        x = 7
    print('yo')

if __name__ == '__main__':
    try:
        test()
    except MyExc as ex:
        print(ex.locals)