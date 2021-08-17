# так работает стек вызовов на примере списка:

x = [1, 2, 3]
x.append(4)
x.append(5)

print(x) # [1, 2, 3, 4, 5]

top = x.pop()
print(top) # 5
print(x) # [1, 2, 3, 4]