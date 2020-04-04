"""
CP1404 Practical
Word occurrence finder.
"""

# Enter custom text and the program will print the number of times each word occurs (alphabetically):
text = "One One was a race horse, Two Two was one too, One One won one race, Two Two won one too."

# Dictionary to store each word and the number of mentions:
word_matrix = {}

text_edit = text.replace(".", '').replace(",", '')   # Remove any commas and fullstops.
text_split = text_edit.lower().split(" ")            # Convert to lower case and split at spaces.

max_len = len(max(text_split, key=len))              # Find the length of the longest word.

for word in text_split:
    if word not in word_matrix:
        # Add word entry.
        word_matrix[word] = 1
    else:
        # Increment word count.
        word_matrix[word] += 1

for k in sorted(list(word_matrix.keys())):
    print("{:{}} : {:2}".format(k, max_len, word_matrix[k]))
