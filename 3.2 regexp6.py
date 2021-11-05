import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"human", r"computer", line))

'''Sample Input:
I need to understand the human mind
humanity

Sample Output:
I need to understand the computer mind
computerity
'''