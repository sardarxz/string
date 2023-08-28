s = input()
s0 = input()
if s0 in s:
    print(s.rsplit(s0, 1)[0])
else:
    print(s)