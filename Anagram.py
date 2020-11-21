# Implementation of Anagrams

# Two strings are anagrams if they are made up of the same letters arranged differently(ignoring the case).
# Examples:
# (1) ''Silent' &  'Listen'
# (2) 'This is a string', 'Is this a string'

# string1 = 'Silent'
# string2 = 'Listen'

# 1. Convert the string to lower case
# print(string1.lower())

# 2. sort the letters using sorted() method, this creates a list of letters like ['e', 'i', 'l', 'n', 's', 't']
# print(sorted(string1.lower()))

# 3. Use join() function to construct the string back again
# print("".join(sorted(string1.lower())))


def check_anagram(first_str: str, second_str: str) -> bool:
    """
    Two strings are anagrams if they are made of the same letters
    arranged differently (ignoring the case).
    """
    return (
            "".join(sorted(first_str.lower())).strip()
            == "".join(sorted(second_str.lower())).strip()
    )


if __name__ == "__main__":
    string1 = input("Enter 1st String : \n")
    string2 = input("Enter 2nd String : \n")

    status = check_anagram(string1, string2)
    print(f"{string1} & {string2} are {'' if status else 'not '}anagrams.")