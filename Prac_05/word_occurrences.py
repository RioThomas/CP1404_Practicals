"""
CP1404 Practical
Word occurrence finder.
"""

text = "One One was a race horse, Two Two was one too, One One won one race, Two Two won one too."
word_matrix = {}

text = text.replace(".", '').replace(",", '')
text_split = text.lower().split(" ")

max_len = len(max(text_split, key=len))

for word in text_split:
    if word not in word_matrix:
        word_matrix[word] = 1
    else:
        word_matrix[word] += 1

for entry in word_matrix:
    print("{:{}} : {:2}".format(entry, max_len, word_matrix[entry]))
