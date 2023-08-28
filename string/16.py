satr=input()
low=''
for i in satr:
    if i>='A' and i<='Z':
        low=low+i.lower()
    else:
        low=low+i
print(low)