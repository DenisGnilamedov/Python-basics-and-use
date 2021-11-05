import sys
import re

pattern = r"\bcat\b"

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

'''Sample Input:
cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?

Sample Output:
cat
catapult and cat
"cat"
!cat?'''