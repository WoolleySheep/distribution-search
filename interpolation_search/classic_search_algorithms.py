from interpolation_search import _first_occurance_binary_method

# Unsorted methods


def sequential_search(array: list, element) -> int:
    for idx, array_el in enumerate(array):
        if array_el == element:
            return idx

    raise ValueError(f"'{element}' is not in list")


# Sorted methods


def jump_search(array: list, element, jump_len: int) -> int:

    if jump_len < 1:
        raise ValueError(f"Jump length ({jump_len}) must be >= 1")

    last_idx = len(array) - 1
    block_start = 0
    block_end = min(jump_len - 1, last_idx)
    while array[block_end] < element:
        if (block_start := block_end) == last_idx:
            raise ValueError(f"'{element}' is not in list")
        block_end = min(block_end + jump_len, last_idx)

    for idx in range(block_start, block_end + 1):
        if array[idx] == element:
            return idx

    raise ValueError(f"'{element}' is not in list")


def _binary_search_recursive(array: list, element, start: int, end: int) -> int:
    """Code ripped from https://stackabuse.com/binary-search-in-python/"""

    if start > end:
        raise ValueError(f"'{element}' is not in list")

    mid = (start + end) // 2
    if (mid_value := array[mid]) == element:
        # TODO: Implement multiple occurance code
        return _first_occurance_binary_method(array, start, mid)

    if element < mid_value:
        return _binary_search_recursive(array, element, start, mid - 1)
    else:
        return _binary_search_recursive(array, element, mid + 1, end)


def binary_search(array: list, element) -> int:

    return _binary_search_recursive(array, element, 0, len(array))


def exponential_search(array: list, element) -> int:
    """Code ripped from https://www.geeksforgeeks.org/exponential-search/?ref=lbp"""

    if array[0] == element:
        return 0

    last_idx = len(array) - 1
    block_end = 1
    while block_end <= last_idx and array[block_end] < element:
        block_end *= 2

    return _binary_search_recursive(
        array, element, block_end // 2, min(last_idx, block_end)
    )
