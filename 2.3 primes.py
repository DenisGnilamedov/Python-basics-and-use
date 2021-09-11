from sympy import *


def primes():
    n = 1
    while True:
        n += 1
        if isprime(n):
            yield n
        else:
            continue

p = primes()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))