import re

s = input()
s1 = input()
s2 = input()
print(re.sub(s1 + '$', s2, s))