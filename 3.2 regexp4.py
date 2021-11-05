import sys
import re

s = r"\\"
for line in sys.stdin:
    line = line.rstrip()
    if re.findall(s, line):
        print(line)

'''Sample Input:
\w denotes word character
No slashes here

Sample Output:
\w denotes word character
'''