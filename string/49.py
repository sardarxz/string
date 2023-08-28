s = input().upper()
words = s.split()
for i in range(len(words)):
    words[i] = '.' * (len(words[i]) - 1) + words[i][-1]
print(' '.join(words))