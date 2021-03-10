objects = [1, 2, 3, 1, 2, "xsad", "xsad"]
a = set()
for obj in objects:
    a.add(id(obj))
print(len(a))
