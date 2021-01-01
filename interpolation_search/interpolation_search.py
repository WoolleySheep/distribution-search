# Author: Matthew Woolley
# Email: matt.wool@live.com.au


def _first_occurance_binary_method(array, min_idx, match_idx):

    if (delta_idx := match_idx - min_idx) <= 0:
        return match_idx

    halfway_idx = delta_idx // 2 + min_idx

    if array[halfway_idx] == array[match_idx]:
        return _first_occurance_binary_method(array, min_idx, halfway_idx)
    else:
        return _first_occurance_binary_method(array, halfway_idx + 1, match_idx)


def _interpolate_index(element, min_idx, max_idx, min_value, max_value):

    if (value_range := max_value - min_value) == 0:
        return min_idx

    normalised_interpolated_value = (element - min_value) / value_range
    delta_idx = max_idx - min_idx
    return int(normalised_interpolated_value * delta_idx) + min_idx


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
