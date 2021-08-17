class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0
class MyList(list, EvenLengthMixin):
    pass

print(MyList.mro())
# [<class '__main__.MyList'>, <class 'list'>, <class '__main__.EvenLengthMixin'>, <class 'object'>]
x = MyList([1, 2, 3])
print(x.even_length()) # False
x.append(4) # сначала берет append из list, затем проверяет четность в Mixin
print(x.even_length()) # True

# также работает для других классов, например для словаря:
class MyDict(dict, EvenLengthMixin):
    pass
print(MyDict.mro())
# [<class '__main__.MyDict'>, <class 'dict'>, <class '__main__.EvenLengthMixin'>, <class 'object'>]
y = MyDict()
y["key"] = "value"
print(y.even_length()) # False
y["key2"] = "value2"
print(y, y.even_length()) # True

# можно задавать то же имя метода, что и у родительского класса:
class MyList2(list, EvenLengthMixin):
    def pop(self):
        z = super(MyList2, self).pop() # super нужен для вызова метода из родительского класса сразу. Здесь ищет метод pop в родителях класса MyList2, в порядке MRO
        print("Last value is", z)
        return z
ml2 = MyList2([1, 2, 4, 17])
v = ml2.pop() # Last value is 17 , сначала вызывается метод pop класса MyList2
print(v) # 17
print(ml2) # [1, 2, 4]