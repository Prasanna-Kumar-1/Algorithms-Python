# Implementation of capitalize the first letter of a sentence or a word

from string import ascii_lowercase, ascii_uppercase

sentence = 'hello world'

# Step1 : create a dictionary of lower case and upper case letters using ascii_lowercase & ascii_uppercase.
#         dictionary = {key: lowercase, value: uppercase)

# Step2 : Loop through dictionary and convert each lc(lowercase) into uc(uppercase)

print(ascii_lowercase)
print(ascii_uppercase)

lower_to_upper = {lc: uc for lc, uc in zip(ascii_lowercase, ascii_uppercase)}

# Get the capitalized version of first letter using value of key1 and append rest of the word
print(lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:])
