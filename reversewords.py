def reverse_words(sentence: str) -> str:
    """
    Function to reverse words
    :param sentence:
    :return:
    """

    list1 = sentence.split()
    return " ".join(list1[::-1])


if __name__ == "__main__":
    result = reverse_words("I love Python")
    print("\n sentence after reversing words is : " + result)