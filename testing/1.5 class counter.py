'''class Counter:
    def __init__(self, start=0):
        self.count = start


x1 = Counter(10)
x = Counter()
print(x1.count)
'''
class A:
    def __init__(self, val=0):
        self.val = val

    def add(self, x):
        self.val += x

    def print_val(self):
        print(self.val)


a = A()
b = A(2)
c = A(4)
a.add(2)
b.add(2)

a.print_val()
b.print_val()
c.print_val()