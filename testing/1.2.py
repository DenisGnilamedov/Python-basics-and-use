'''x = [1, 2, 3]
print(id(x))    # 2241892781696
print(id([1, 2, 3]))    # 2241892791104

x = [1, 2, 3]
y = x
y is x  # True
y is [1, 2, 3]  # False
'''
x = [1, 2, 3]
y = x
y.append(4)
print(str(x))
print(y)

s = "123"
s = s+"4"
print(s)