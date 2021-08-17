'''def printab(a, b, *args):
    print("a", a)
    print("b", b)
    print("add arg:")
    for arg in args:
        print(arg)
printab(10, 20, 30, 40, 50)

def printab(a, b, **kwargs):
    print("a", a)
    print("b", b)
    print("add arg:")
    for key in kwargs:
        print(key, kwargs[key])
printab(10, c=30, d=40, f=1, b=20)

def s(a, *vs, b=10):
    print(a)
    print(*vs)
    print(b)
    res = a + b
    for v in vs:
        res += v
    return res


print(s(11,10,10))
'''
#################################
# функция Фибаначчи 1 1 2 3 5 8 13...
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
y = fib(5)
print(y)