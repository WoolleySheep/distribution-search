def _uniform_index_estimate(element, len_array, min, max):

    percentage_estimate = (element - min) / (max - min)
    index_estimate = int(round(len_array * percentage_estimate))
    if index_estimate > len_array - 1:
        return len_array - 1
    elif index_estimate < 0:
        return 0
    else:
        return index_estimate

def _gone_past(increment, value, element):

    if (increment == 1 and value > element) or (increment == -1 and value < element):
        return True
    return False



def get_index(array, element, min, max):

    if not (min <= element <= max):
        raise ValueError(f"'{element}' is not in list")

    idx = _uniform_index_estimate(element, len(array), min, max)

    increment = 1 if array[idx] < element else -1

    while array[idx] != element:
        idx += increment
        if not (0 <= idx <= len(array)) or _gone_past(increment, array[idx], element):
            raise ValueError(f"'{element}' is not in list")

    while (idx_minus_one := idx - 1) >= 0 and array[idx_minus_one] == element:
        idx = idx_minus_one
    
    return idx


x = [1, 2, 2, 4, 5]
print(x.index(2))





