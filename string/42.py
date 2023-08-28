s = input().upper()
words = s.split()
count = 0
for word in words:
    if word[0] == word[-1]:
        count += 1
print(count)