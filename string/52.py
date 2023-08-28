sentence = "сигма момент"

words = sentence.split()

capitalized_words = [word.capitalize() for word in words]

capitalized_sentence = " ".join(capitalized_words)

print(capitalized_sentence)