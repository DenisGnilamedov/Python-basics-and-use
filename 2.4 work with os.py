import zipfile
import os
import os.path
import glob

with zipfile.ZipFile("C:/1/main.zip", 'r') as zip_file:
    zip_file.extractall("C:/1/")
for dirpath, dirname, files in os.walk("C:/1/main"):
    if glob.glob("*.py"):
        answer = "\n".join(dirname)


'''with open("C:/1/2_4.txt", 'a') as ouf:
    ouf.write(answer)'''
