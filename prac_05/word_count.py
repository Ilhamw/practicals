unique_words = {}
string_input = input("Text: ")

words = string_input.split()
for word in words:
    occurences = unique_words.get(word, 0)
    unique_words[word] = occurences + 1

words = list(unique_words.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))
