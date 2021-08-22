n = int(input())
d = {}
for i in range(n):
    child, *parent = input().replace(":", " ").split()
    if child not in d:
        d.update({child: parent})
    else:
        d[child] += parent

q = int(input())
for i in range(q):
    errname = int(input())
