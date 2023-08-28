s = input().upper()
words = s.split()
for i in range(len(words)):
    words[i] = words[i][0] + '.' * (len(words[i]) - 1)
print(' '.join(words))