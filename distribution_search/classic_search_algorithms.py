def sequential_search(array: list, element) -> int:
    for idx, array_el in enumerate(array):
        if array_el == element:
            return idx
    
    raise ValueError(f"'{element}' is not in list")

def binary_search(array: list, element) -> int:

    return binary_search_recursive(array, element, 0, len(array))

def binary_search_recursive(array: list, element, start: int, end: int) -> int:
    """Code ripped from https://stackabuse.com/binary-search-in-python/"""

    if start > end:
        raise ValueError(f"'{element}' is not in list")

    mid = (start + end) // 2
    mid_value = array[mid]
    if element == mid_value:
        return mid

    if element < mid_value:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)
