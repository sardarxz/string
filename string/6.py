c=input()
if len(c)==1:
    n=ord(c)
    if ((n>=64) and (n<=90)) or ((n>=97) and (n<=122)):
        print('lotin')
    elif n>=48 and n<=57:
        print('digit')
    else:
        print('rus')