# Итератор, который перечисляет случайные элементы, до тех пор, пока не выведет нам нужное число элементов:

from random import random


class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration
'''x = RandomIterator(3)
print(next(x)) # next(x) - x.__next__() x -- iterator
print(next(x))
print(next(x))
print(next(x))'''


for x in RandomIterator(10):
    print(x)

# чтобы объект можно было проитерировать (перечислить его элементы), у него должен быть определен
# метод __iter__, который возвращает нам итератор, а чтобы объект являлся итератором,
# у него должен быть определен метод __next__.