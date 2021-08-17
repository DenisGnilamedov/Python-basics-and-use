# создаем класс MyList, который будет наследоваться от листа (списка) и создаем метод even_length, проверяющий, является-ли лист четной длины
class MyList(list):
    def even_length(self):
        return len(self) % 2 == 0

# создаем экземпляр x
x = MyList()
print(x) # []
# заполняем список элементами
x.extend([1, 2, 3, 4, 5])
print(x) # [1, 2, 3, 4, 5] (взято из класса list)
print(x.even_length()) # False (взято из MyList)
x.append(6)
print(x.even_length()) # True

print(isinstance(x, object))