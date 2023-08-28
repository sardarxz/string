s = input().upper()
words = s.split()
count = 0
for word in words:
    if word.count('А') == 3:
        count += 1
print(count)