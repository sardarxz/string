s = input().upper()
words = s.split()
count = 0
for word in words:
    if 'А' in word:
        count += 1
print(count)