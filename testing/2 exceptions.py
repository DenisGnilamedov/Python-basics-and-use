#пропустить исключение, продолжить выполнение программы:
'''try:
    x = [1, 2, "hello", 7]
    x.sort()
    print(x)
except TypeError:
    print("Type error")

print("I can catch")
######################################

def f(x, y):
    try:
        return x/y
    except TypeError:
        print("Type error")
    except ZeroDivisionError:
        print("Zero division")


print(f(5, 0)) #выдаст Zero division; None

######################################

def f(x, y):
    try:
        return x/y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)


print(f(5, 0))
print(f(5, []))
'''
#Output:
'''<class 'ZeroDivisionError'>
division by zero
('division by zero',)
None
<class 'TypeError'>
unsupported operand type(s) for /: 'int' and 'list'
("unsupported operand type(s) for /: 'int' and 'list'",)
None'''
######################################

def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("div by 0")
    else:
        print("result is", result)
    finally:
        print("finally")


divide(2, 1)
divide(2, 0)
divide(2, [])
'''result is 2.0
finally
div by 0
finally
finally
Traceback (most recent call last):
  File "C:\Users\DENIS_PC\PycharmProjects\Python-basics-and-use\for testing\2 exceptions.py", line 61, in <module>
    divide(2, [])
  File "C:\Users\DENIS_PC\PycharmProjects\Python-basics-and-use\for testing\2 exceptions.py", line 50, in divide
    result = x/y
TypeError: unsupported operand type(s) for /: 'int' and 'list'''