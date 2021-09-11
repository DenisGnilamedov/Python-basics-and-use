
a = [i + 1 for i in range(4)] # [1, 2, 3, 4]

b = [i for i in range(4)] # [0, 1, 2, 3]

c = [i for i in range(5)][1:] # [1, 2, 3, 4]

d = list(i + 1 for i in range(4)) # [1, 2, 3, 4]

print(a,b,c,d, end=' ')