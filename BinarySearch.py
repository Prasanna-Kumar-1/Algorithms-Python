def binary_search(sorted_collection, item):
    """Implementation of binary search algorithm in Python. Collection must be ascending sorted
    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found
    """


def binary_search(input_list, item):
    first = 0
    last = len(input_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if input_list[midpoint] == item:
            found = True
        else:
            if item < input_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def __assert_sorted(collection1):
    """Check if collection is ascending sorted, if not - raises :py:class:`ValueError`
    :param collection: collection
    :return: True if collection is ascending sorted
    :raise: :py:class:`ValueError` if collection is not ascending sorted
    ...
    ValueError: Collection must be ascending sorted
    """
    if collection != sorted(collection):
        raise ValueError("Collection must be ascending sorted")
    return True


if __name__ == "__main__":
    import sys

    user_input = input("Enter numbers separated by comma:\n").strip()
    collection = [int(item) for item in user_input.split(",")]
    print(collection)
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit("Sequence must be ascending sorted to apply binary search")

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = binary_search(collection, target)
    if result is not None:
        print(f"{target} found at positions: {result}")
    else:
        print("Not found")
