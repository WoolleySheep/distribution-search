def _interpolate_index(element, min_idx, max_idx, min_value, max_value):

    nelements = max_idx - min_idx + 1
    normalised_interpolated_value = (element - min_value) / (max_value - min_value)
    return int(normalised_interpolated_value * nelements) + min_idx


def _interpolation_search_recursive(array: list, element, min_idx: int, max_idx: int) -> int:

    if min_idx > max_idx:
        raise ValueError(f"'{element}' is not in list")

    interpol_idx = _interpolate_index(element, min_idx, max_idx, array[min_idx], array[max_idx])
    interpol_val = array[interpol_idx]

    if element == interpol_val:
        return interpol_idx

    if element < interpol_val:
        return _interpolation_search_recursive(array, element, min_idx, interpol_idx-1)
    else:
        return _interpolation_search_recursive(array, element, interpol_idx+1, max_idx)


def interpolation_search(array: list, element) -> int:

    return _interpolation_search_recursive(array, element, 0, len(array) - 1)


x = [1, 2, 3, 5, 6, 8, 9]
e = 2
print(interpolation_search(x, 2))