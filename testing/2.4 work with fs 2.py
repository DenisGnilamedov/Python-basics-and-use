import os
import os.path
import shutil
os.chdir("C:/1") # сменить директорию
for curr_dir, dirs, files in os.walk("."): # пройтись по всем директориям из текущей "."
    print(dirs)

'''print(os.listdir()) # список файлов в текущей директории
print(os.getcwd()) # узнать текущую директорию
print(os.path.exists("1.2.py")) # узнать существует-ли файл
print(os.path.isfile("1.3 (2).py")) # является-ли файлом?
print(os.path.isdir("2.4 work with fs 2.py")) # является-ли папкой?
print(os.path.abspath("1.3 (2).py")) # узнать абсолютный путь из относительного'''
shutil.copy("c:/1/test.txt", "c:/1/test228.txt") # копировать файл
# shutil.copytree("C:/1", "C:/1/1") # копировать папку