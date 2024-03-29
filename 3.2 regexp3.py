import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"z(.{3}z)", line):
        print(line)

'''Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:
zabcz
zzxzz
'''