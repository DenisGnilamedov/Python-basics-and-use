import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\b(\w)(\w)", r"\2\1", line))


'''Sample Input:
this is a text
"this' !is. ?n1ce,

Sample Output:
htis si a etxt
"htis' !si. ?1nce,
'''