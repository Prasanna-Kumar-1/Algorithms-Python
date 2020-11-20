# Implementation of simple binary search using recursion

from __future__ import annotations


def binary_search(a_list: list[int], item: int) -> bool:
    """
    """
    # Check if the list is empty; if it is empty, return false
    if len(a_list) == 0:
        return False
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    if item < a_list[midpoint]:
        return binary_search(a_list[:midpoint], item)
    else:
        return binary_search(a_list[midpoint + 1:], item)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma : \n").strip()
    # Create a list from the input items entered

    # sequence = [int(item) for item in user_input.split(",")]

    sequence = [int(item) for item in user_input.split(",")]
    print(sequence)
    target = int(input("Enter the number to be searched in the list: \n").strip())
    not_str = "" if binary_search(sequence, target) else "not"
    print(f"{target} is {not_str}found in {sequence}")
