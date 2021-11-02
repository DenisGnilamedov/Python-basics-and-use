import re

# print(re.match) # берет шаблон, берет строку и проверяет, подходит ли строка под шаблон.
# print(re.search) # находит первую подстроку, подходящую под шаблон
# print(re.findall) # находит все подстроки, подходящие под шаблон
# print(re.sub) # заменить все подходящие подстроки чем-нибудь

# [] - можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# \d - [0-9] -- цифры
# \D - [^0-9] -- все, кроме цифр
# \s - [ \t\n\r\f\v ] - пробельные символы
# \S - [^ \t\n\r\f\v ] - все, кроме пробельных символов
# \w - [a-zA-Z0-9_] - все буквы, цифры + _
# \W - [^ a-zA-Z0-9_] - все, кроме буквы, цифры + _
# . - под точку подходит любой символ, кроме переноса строки
"""
pattern = r"abc"
string = "abcd"
match_object = re.match(pattern, string)
print(match_object) # <re.Match object; span=(0, 3), match='abc'>
"""
"""
pattern = r"a[abc]c"
string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions) # ['abc', 'acc', 'aac']

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos) # abc, abc, abc
"""

pattern = r"ab*a" # * после b значит, что хотим найти любое вхождение, где есть любое число символов "b", включая 0 ['aa', 'aba', 'abba']
pattern_2 = r"ab+a" # + после b значит, что хотим найти любое вхождение, где число символов "b" больше 0
# ab?a - 0 или 1 вхождение символа b
# ab{3}a - если нужно именно 3 символа b
# ab{2,4}a - от 2 до 4 вхождений
# test|text - подойдет ИЛИ test, ИЛИ text

string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions) # ['aa', 'aba', 'abba']