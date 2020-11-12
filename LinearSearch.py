# Implementation of linear search


def linear_search(sequence: list, target: int) -> int:
    """Implementation of a linear search algorithm
    :param sequence: a collection with comparable items (as sorted items not required in Linear Search)
    :param target: item value to search
    :return: index of found item or None if item is not found
    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
            print(index)
    return -1


if __name__ == '__main__':
    user_input = input("Enter the list of numbers seperated by comma: \n").strip()
    # Take each item from user_input, split by , and convert it into int and then create a sequence
    sequence = [int(item) for item in user_input.split(",")]
    print(sequence)

    target = int(input("Enter the number to be searched : \n").strip())
    search_result = linear_search(sequence, target)

    if search_result != -1:
        print(f"linear_search({sequence}, {target}) & {target} is found at the position : {search_result}")
    else:
        print(f"{target} is not found in {sequence}")
