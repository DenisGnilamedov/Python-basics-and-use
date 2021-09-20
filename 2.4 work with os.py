import zipfile
import os
import os.path
import glob

a = []
with zipfile.ZipFile("C:/1/main.zip", 'r') as zip_file:
    zip_file.extractall("C:/1/")
os.chdir("C:/1/")
for dirpath, dirname, files in os.walk(r"."):
    for file in files:
        if file[-3:] == '.py':
            print(dirpath[2:])
            break

