# напишем класс итератора, который принимает список элементов, которые мы хотим перебирать парами в конструктор:

class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0 # число элементов, которые мы уже перебрали

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1] # выводим 2 элемента списка парой
        else:
            raise StopIteration

# наследуемся от класса list таким образом, чтобы каждый раз, когда мы итерировались по
# объекту класса MyList, мы бы перебирали элементы парами
class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)

for pair in MyList([1, 2, 3, 4, 5]):
    print(pair) # (1, 2)
                # (3, 4)
                # IndexError: list index out of range , т.к. не находит пары для 5