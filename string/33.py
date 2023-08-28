s = input()
s0 = input()
if s0 in s:
    print(s.replace(s0, "", 1))
else:
    print(s)