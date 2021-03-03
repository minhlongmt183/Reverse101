from z3 import *

s = Solver()
a = Int('a')
b = Int('b')

s.add(a > 2)
s.add(b < 5)
s.add(a + b == 6)

s.check()
s.model()