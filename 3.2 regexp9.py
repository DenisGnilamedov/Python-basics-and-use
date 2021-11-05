import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"(\w)(\1*)", r"\1", line))

'''Sample Input:
attraction
buzzzz

Sample Output:
atraction
buz
'''