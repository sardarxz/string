satr = input()
lot=0
kri=0
for i in satr:
    if i>='a' and i<='z':
        lot +=1 
    elif i>='а' and i<='я':
        kri +=1

if (lot==0) and (kri == 0):
    print('нет')
else :
    print(lot)
    print(kri)