


class A:
    A = 0
    def __init__(self,v):
        self._a = v + 1

    def f(self):
        return 1

    def g():
        return self.f()


    def a(self):
        print('a')
    def set(self, v):
        self.v = v
        return v

class B:
    def __init__(self):
        A.__init__(self)

    def a(self):
        print('b')

    def __str__(self):
        return 'b'

class C(A, B):
    def c(self):
        self.a()

def fun(x):
    try:
        x = x / x
    except:
        print('a', end = '')
    else:
        print('b', end ='')
    finally:
        print('c', end = '')

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v

class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.args = (msg,)

def o(p):
    def q():
        return '*'*p
    return q

def f(par2, par1):
    return par2 + par1

d = {
    1:0,
    2:1,
    3:2,
    0:1
}
x = 0

for y in range(len(d)):
    x = d[x]

def fun(x):
    return 1 if x%2 != 0 else 2

x = """
"""
a = True
b = False
a = a or B
b = a and b
a = a or B

d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]

d = {
    'one': 1,
    'three': 3,
    'two': 2
}

def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s

def fun(d,k,v):
    d[k] = v


print(issubclass(C,A) and issubclass(C,B))