sentence = "Это предложение на русском языке."
words = sentence.split()
shortest_word = min(words, key=len)
print(shortest_word)