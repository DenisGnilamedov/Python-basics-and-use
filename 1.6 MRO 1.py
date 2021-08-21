def find_path(d, end, start, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in d:
        return None
    for node in d[start]:
        if node not in path:
            newpath = find_path(d, end, node, path)
            if newpath: return newpath
    return None


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
    parent, child = input().split(" ")
    find_path(d, parent, child)
    if find_path(d, parent, child) == None:
        print("No")
    else:
        print("Yes")