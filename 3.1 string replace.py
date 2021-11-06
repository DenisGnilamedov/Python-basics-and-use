s = input()
a = input()
b = input()
count = 0
a_in_s = s.count(a)
for i in range(1001):
    if s.count(a) > a_in_s:
        print('Impossible')
        break
    if a in s:
        s = s.replace(a, b)
        count += 1
    else:
        print(count)
        break
    if count > 1000:
        print('Impossible')


