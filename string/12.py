satr=input()
n=int(input())
m='*'*n
for i in satr:
    if i==satr[-1]:
        print(i,end='')
    else:
        print(i,end=m)