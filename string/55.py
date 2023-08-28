sentence = "Это предложение на русском языке."
words = sentence.split()
longest_word = max(words, key=len)
print(longest_word)