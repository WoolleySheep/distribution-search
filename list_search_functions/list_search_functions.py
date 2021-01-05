# Unsorted list search methods


def linear_search(array: list, element) -> int:
    for idx, array_el in enumerate(array):
        if array_el == element:
            return idx

    raise ValueError(f"'{element}' is not in list")


# Sorted list search methods


def jump_search(array: list, element, jump_len: int) -> int:

    if not array:
        raise ValueError(f"'{element}' is not in list")

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


def _first_occurance_binary_method(array, min_idx, match_idx):

    if (delta_idx := match_idx - min_idx) <= 0:
        return match_idx

    halfway_idx = delta_idx // 2 + min_idx

    if array[halfway_idx] == array[match_idx]:
        return _first_occurance_binary_method(array, min_idx, halfway_idx)
    else:
        return _first_occurance_binary_method(array, halfway_idx + 1, match_idx)


def _binary_search_recursive(array: list, element, start: int, end: int) -> int:
    """Code based on https://stackabuse.com/binary-search-in-python/"""

    if start > end:
        raise ValueError(f"'{element}' is not in list")

    mid = (start + end) // 2
    if (mid_value := array[mid]) == element:
        return _first_occurance_binary_method(array, start, mid)

    if element < mid_value:
        return _binary_search_recursive(array, element, start, mid - 1)
    else:
        return _binary_search_recursive(array, element, mid + 1, end)


def binary_search(array: list, element) -> int:

    if not array:
        raise ValueError(f"'{element}' is not in list")

    return _binary_search_recursive(array, element, 0, len(array) - 1)


def exponential_search(array: list, element) -> int:
    """Code based on https://www.geeksforgeeks.org/exponential-search/?ref=lbp"""

    if not array:
        raise ValueError(f"'{element}' is not in list")

    if array[0] == element:
        return 0

    last_idx = len(array) - 1
    block_end = 1
    while block_end <= last_idx and array[block_end] < element:
        block_end *= 2

    return _binary_search_recursive(
        array, element, block_end // 2, min(last_idx, block_end)
    )


def fibonacci_search(array: list, element) -> int:
    """Code based on https://www.geeksforgeeks.org/fibonacci-search/"""

    if not array:
        raise ValueError(f"'{element}' is not in list")

    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2

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
            block_start = fib_idx
            fib3 = fib2
            fib2 = fib1
            fib1 = fib3 - fib2

        else:
            fib3 = fib1
            fib2 = fib2 - fib1
            fib1 = fib3 - fib2

    if array[block_start] == element:
        return block_start

    raise ValueError(f"'{element}' is not in list")


def _interpolate_index(element, min_idx, max_idx, min_value, max_value):

    if (value_range := max_value - min_value) == 0:
        return min_idx

    normalised_interpolated_value = (element - min_value) / value_range
    delta_idx = max_idx - min_idx
    return int(round(normalised_interpolated_value * delta_idx)) + min_idx


def _interpolation_search_recursive(
    array: list, element, min_idx: int, max_idx: int
) -> int:

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
        return _interpolation_search_recursive(
            array, element, min_idx, interpol_idx - 1
        )
    else:
        return _interpolation_search_recursive(
            array, element, interpol_idx + 1, max_idx
        )


def interpolation_search(array: list, element) -> int:

    return _interpolation_search_recursive(array, element, 0, len(array) - 1)
