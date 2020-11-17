# Implementation of sentinel search

# Standard Linear Search : A standard linear search would go through all the elements checking the array index
#                          every time to check when it has reached the last element

# Example:
# for (int i = 0; i < length; i++)
#    {
#     if (array[i] == elementToSearch)
#     {
#         return i;
#     }
#    }

# sentinel search        : But, the idea is sentinel search is to keep the element to be searched in the end, and
#                          to skip the array index searching, this will reduce one comparison in each iteration.

# Example:
# while(a[i] != element)
#     i++;

# Here, we are not checking for array index searching

def sentinel_linear_search(sequence, target):
    """Implementation of sentinel linear search algorithm in Python
    :param sequence: some sequence with comparable items
    :param target: item value to search
    :return: index of found item or None if item is not found
    """

    # Append the element to be searched at the end of the sequence
    sequence.append(target)

    # Loop through each element of the sequence equating if it is equal to target
    # if it is not equal, increase the index and loop through
    index = 0
    while sequence[index] != target:
        index += 1

    # Remove the element
    sequence.pop()

    if index == len(sequence):
        return None

    return index


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item) for item in user_input.split(",")]

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)

    result = sentinel_linear_search(sequence, target)

    if result is not None:
        print(f"{target} found at the position: {result}")
    else:
        print(f"{target} is NOT found")
