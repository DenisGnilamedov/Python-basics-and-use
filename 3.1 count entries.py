s = input()
t = input()
count = 0
i = 0
if t not in s:
    print(0)
else:
    while True:
        i = s.find(t, i)
        if i == -1:
            break
        count += 1
        i = i + 1
    print(count)
