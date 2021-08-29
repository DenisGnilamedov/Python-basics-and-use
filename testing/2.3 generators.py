from random import random

'''
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
'''
def random_generator(k): # сколько случайных чисел из диапазона 0-1 мы бы хотели вывести.
    for i in range(k):
        yield random()
gen = random_generator(3)
print(type(gen)) # <class 'generator'>
for i in gen:
    print(i)

# Генераторы - удобный синтаксис для написания итераторов.
