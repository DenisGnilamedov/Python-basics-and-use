import sys
import re

pattern = r"(cat.*?){2,}"

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

'''Sample Input:
catcat
cat and cat
catac
cat
ccaatt

Sample Output:
catcat
cat and cat'''