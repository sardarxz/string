sentence = "строка-предложение на русском языке"
vowels = "аеёиоуыэюя"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print(count)