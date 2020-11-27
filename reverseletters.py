def reverse_letters(sentence: str) -> str:
    """
    Reverses letters in a given string without adjusting the position of the words
    :param sentence:
    :return:
    """

# use split() function to create a list from the input
    str1 = sentence.split()
    print(str1)

# output : ['The', 'cat', 'in', 'the', 'hat']

# for each item or word in this list, loop through and replace each word with word[::-1]
# combine all of them to construct a string using join() function
    return " ".join(word[::-1] for word in str1)


if __name__ == "__main__":
    result = reverse_letters("The cat in the hat")
    print("\n Sentence after reversing letters is : " + result)