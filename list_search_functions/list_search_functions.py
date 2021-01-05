"""
-----------------------------
Author: Matthew Woolley
Email: matt.wool@live.com.au
-----------------------------

A collection of list-searching functions, utilising various algorithms
"""

# UNSORTED LIST SEARCH FUNCTIONS


def linear_search(array: list, element, start_idx=None, stop_idx=None) -> int:
    # Iterate through the array until the element is encountered
    if start_idx is None:
        start_idx = 0
    if stop_idx is None:
        stop_idx = len(array) - 1

    for idx in range(start_idx, stop_idx + 1):
        if array[idx] == element:
            return idx

    raise ValueError(f"'{element}' is not in list")


# SORTED LIST SEARCH FUNCTIONS


def jump_search(array: list, element, jump_len: int) -> int:

    if not array:
        raise ValueError(f"'{element}' is not in list")

    if jump_len < 1:
        raise ValueError(f"Jump length ({jump_len}) must be >= 1")

    last_idx = len(array) - 1
    block_start = 0
    block_end = min(jump_len - 1, last_idx)
    # Check whether the last value in the block is
    # greater than the search element
    while array[block_end] < element:
        if (block_start := block_end) == last_idx:
            raise ValueError(f"'{element}' is not in list")
        block_end = min(block_end + jump_len, last_idx)

    # Once the block which might contain the element in found, revert to linear search
    return linear_search(array, element, block_start, block_end)


def binary_search(
    array: list, element, start_idx: int = None, stop_idx: int = None
) -> int:
    """Code based on https://stackabuse.com/binary-search-in-python/"""

    if start_idx is None:
        start_idx = 0
    if stop_idx is None:
        stop_idx = len(array) - 1

    if start_idx > stop_idx:
        raise ValueError(f"'{element}' is not in list")

    mid = (start_idx + stop_idx) // 2
    if (mid_value := array[mid]) == element:
        # Find the first occurance of the element
        return _first_occurance_binary_method(array, start_idx, mid)

    if element < mid_value:
        return binary_search(array, element, start_idx, mid - 1)
    else:
        return binary_search(array, element, mid + 1, stop_idx)


def exponential_search(array: list, element) -> int:
    """Code based on https://www.geeksforgeeks.org/exponential-search/?ref=lbp"""

    if not array:
        raise ValueError(f"'{element}' is not in list")

    # Cannot search first element using exponential algorithm
    if array[0] == element:
        return 0

    last_idx = len(array) - 1
    block_end = 1
    # Expand the size of the search block until it is longer than the list
    # or its final element is larger than the search element
    while block_end <= last_idx and array[block_end] < element:
        block_end *= 2

    # Once the search block has been established, revert to binary search
    return binary_search(array, element, block_end // 2, min(last_idx, block_end))


def fibonacci_search(array: list, element) -> int:
    """Code based on https://www.geeksforgeeks.org/fibonacci-search/"""

    if not array:
        raise ValueError(f"'{element}' is not in list")

    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2

    # Iterate until the larges fibb no is >= the length of the array
    while fib3 < len(array):
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2

    block_start = 0

    while fib3 > 1:
        fib_idx = min(block_start + fib1, len(array) - 1)
        if array[fib_idx] == element:
            return _first_occurance_binary_method(array, block_start, fib_idx)

        if array[fib_idx] < element:
            # Search the larger right sublist, drop all fib no's by 1 place
            block_start = fib_idx
            fib3 = fib2
            fib2 = fib1
            fib1 = fib3 - fib2

        else:
            # Search the smaller left sublist, drop all fib no's by 2 places
            fib3 = fib1
            fib2 = fib2 - fib1
            fib1 = fib3 - fib2

    if array[block_start] == element:
        return block_start

    raise ValueError(f"'{element}' is not in list")


def interpolation_search(
    array: list, element, min_idx: int = None, max_idx: int = None
) -> int:
    """Assumes that the array is uniformly distributed"""

    if min_idx is None:
        min_idx = 0
    if max_idx is None:
        max_idx = len(array) - 1

    if (
        min_idx > max_idx
        or element < (min_value := array[min_idx])
        or element > (max_value := array[max_idx])
    ):
        raise ValueError(f"'{element}' is not in list")

    interpol_idx = _interpolate_index(element, min_idx, max_idx, min_value, max_value)
    interpol_val = array[interpol_idx]

    if element == interpol_val:
        return _first_occurance_binary_method(array, min_idx, interpol_idx)

    if element < interpol_val:
        return interpolation_search(array, element, min_idx, interpol_idx - 1)
    else:
        return interpolation_search(array, element, interpol_idx + 1, max_idx)


# PRIVATE HELPER FUNCTIONS


def _first_occurance_binary_method(array: list, min_idx: int, match_idx: int) -> int:
    """Returns the lowest index of a given value in a list

    This function is only called once the target value has been found at match_idx.
    The function then uses binary search to find the first occurance of
    the target value in the list"""

    if (delta_idx := match_idx - min_idx) <= 0:
        return match_idx

    halfway_idx = delta_idx // 2 + min_idx

    if array[halfway_idx] == array[match_idx]:
        return _first_occurance_binary_method(array, min_idx, halfway_idx)
    else:
        return _first_occurance_binary_method(array, halfway_idx + 1, match_idx)


def _interpolate_index(
    element, min_idx: int, max_idx: int, min_value, max_value
) -> int:
    """Calculates the estimated element index via interpolation"""

    if (value_range := max_value - min_value) == 0:
        return min_idx

    normalised_interpolated_value = (element - min_value) / value_range
    delta_idx = max_idx - min_idx
    return int(round(normalised_interpolated_value * delta_idx)) + min_idx
