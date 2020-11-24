def naive_pattern_search(s: str, pattern: str):
    """
    :param s: Main String
    :param pattern: Pattern String to be searched
    :return:
    """

    pattern_length = len(pattern)
    position = []
    for i in range(len(s) - pattern_length + 1):
        match_found = True
        for j in range(pattern_length):
            if s[i + j] != pattern[j]:
                match_found = False
                break
            if match_found:
                position.append(i)
                break
    print(f"Pattern found at {position}")


if __name__ == "__main__":
    naive_pattern_search("ABCDEFG", "A")