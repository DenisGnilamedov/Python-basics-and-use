'''
print("abc" in "abcba")# True
print("abce" in "abcba") # False

print("cabcd".find("abc", 1))  # выдать индекс первого вхождения (здесь 1) или -1, если вхождения нет
print("cabcd"[1:].find("abc")) # указываем стартовую позицию (первый элемент), получаем позицию искомого,
                                # исходя из получившегося среза (0)
print(str.find.__doc__) # вызов документации по методу
'''
# print("cabcd".index("abc"))  # найти индекс первого вхождения (1)
# print("cabcd".index("aec")) # если не нашли - ValueError

# s = "The whale in black fled across the desert, and the gunslinger followed"
# print(s.startswith(("The woman", "The dog", "The man in black"))) # проверить, с чего начинается строка, перечисляем
                                                                    # кортеж возможных значений
# print(s.startswith.__doc__)

# s = "image.png"
# print(s.endswith(".png")) # True
'''
s = "abacaba"
print(s.count("aba")) # число вхождений (непересекающихся) в строку (2)
print(s.count.__doc__)
print(s.find("aba")) # [0]
print(s.rfind("aba")) # ищет первое вхождение справа [4]
'''
# s = "The man in black fled across the desert, and the gunslinger followed"
# print(s.lower()) # возвр копию строки в ниж регистре
# print(s.upper()) # возвр копию строки в верх регистре
# print(s.count("the")) # 2
# print(s.lower().count("the")) # 3

# s = "1,2,3,4"
# print(s)
# print(s.replace(",", ", ", 2)) # найти все вхождения в строке (1 арг) и заменить на 2 аргумент,
                                # число замен - 2 (1, 2, 3,4)
# print(s.replace.__doc__)

#s = "1\t\t 2  3       4       "  # ['1', '2', '3', '4']
# print(s.split()) # разделить строку по заданному разделителю, если разделителя нет, убирает лишние строки и отступы
# print(s.split.__doc__)

# s = "_*__1, 2, 3, 4__*_"
# print(repr(s.rstrip("*_"))) # убирает указанные символы из строки
# print(repr(s.lstrip("*_")))
# print(repr(s.strip("*_")))

# numbers = map(str, [1, 2, 3, 4, 5])
# print(repr(" ".join(numbers))) # '1 2 3 4 5'

'''
capital = 'London is the capital of Great Britain'
template = '{} is the capital of {}' # шаблон
print(template.format("London", "Great Britain")) # London is the capital of Great Britain
print(template.format("Vaduz", "Liechtenstein")) # Vaduz is the capital of Liechtenstein
print(template.format.__doc__)
'''

# template = '{capital} is the capital of {country}'
# print(template.format(capital="London", country="Great Britain"))
# print(template.format(country="Liechtenstein", capital="Vaduz"))

'''
import requests
template = "Response from {0.url} with code {0.status_code}"

res = requests.get("https://docs.python.org/3.5/")
print(template.format(res)) # Response from https://docs.python.org/3.5/ with code 200
res = requests.get("https://docs.python.org/3.5/random")
print(template.format(res))
'''
from random import random
x = random()
print(x) # 0.25483347315346105
print("{:.3}".format(x)) # 0.255