n=int(input())
s='Hello world!'

if len(s)>n:

    s=s[-n:]

elif len(s)<n:

    s='.'*(n-len(s))+s
    
print(s)