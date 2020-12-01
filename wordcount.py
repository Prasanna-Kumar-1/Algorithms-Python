# Implementation of word count in a string
def word_count(sentence: str) -> dict:
    # Create a Empty Dictionary
    counts = dict()
    print(counts)

    # Create a list from the input sentence using split() function
    words = sentence.split()

    # Loop through each item in the above list
    for word in words:
        # Check if the item is present in the dictionary
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


if __name__ == "__main__":
    print(word_count("INPUT STRING INPUT"))