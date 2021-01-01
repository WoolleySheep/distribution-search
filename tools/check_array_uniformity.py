from scipy.stats import chisquare


def is_array_uniform(array: list, alpha: float = 0.05):
    """Use the Chi-square statistical test to determine how uniformly
    the elements in a list are distributed
    """

    nsegments = len(array)
    min = x[0]
    max = x[-1]
    segment_size = (max - min) / nsegments

    elements_per_segment = [0] * nsegments

    for element in x[:-1]:
        current_segment = int((element - min) / segment_size)
        elements_per_segment[current_segment] += 1
    
    print(elements_per_segment)

    elements_per_segment[-1] += 1

    chi_squared_result = chisquare(elements_per_segment)
    print(chi_squared_result)

    if chi_squared_result.pvalue > 1 - alpha:
        return True
    
    return False




x = [1, 2, 3, 4, 5, 6, 7, 7]
print(is_array_uniform(x))
