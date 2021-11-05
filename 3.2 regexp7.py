import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\b(a|A)+\b", r"argh", line, count=1)) #можно приписать flags=re.IGNORECASE


'''Sample Input:
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA

Sample Output:
There’ll be no more "argh"
argh AaAaAaA
'''