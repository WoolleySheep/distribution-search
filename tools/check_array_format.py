import matplotlib.pyplot as plt
from scipy.stats import chisquare, kstest
from tabulate import tabulate


def is_array_correct_format(
    array: list, array_type=list, element_type=int, check_uniformity=False, kwargs={}
) -> bool:

    if type(array) is not array_type:
        print(f"Type of array is {type(array)}; should be {array_type}")
        return False

    if not are_all_elements_same_type(array, element_type):
        print(f"Not all elements of the array are of type {element_type}")
        return False

    if not is_array_sorted(array):
        print("Array is not sorted")
        return False

    if check_uniformity and not is_array_uniform(array, **kwargs):
        print("Array elements are not uniformly distributed")
        return False

    return True


def is_array_sorted(array: list) -> bool:

    if len(array) == 0 or len(array) == 1:
        return True

    return all(array[idx] <= array[idx + 1] for idx in range(len(array) - 1))


def are_all_elements_same_type(array: list, element_type) -> bool:

    return all([type(el) is element_type for el in array])


def is_array_uniform(
    array: list,
    alpha: float = 0.05,
    print_test_data: bool = False,
    show_plot: bool = False,
):
    """Analyse the uniformity of the elements in the array

    Utilises the chi-square and kolmogorov-smirnov tests to assess
    how closely the array matches a uniform distribution.  Test p-value
    must be > 1 - alpha (aka: less than an x% chance of not being uniform).
    """

    nsegments = len(array)

    bin_values, _, _ = plt.hist(array, nsegments)

    chi_squared_result = chisquare(bin_values)
    chi_squared_pass = chi_squared_result.pvalue > 1 - alpha

    kstest_result = kstest(
        array, "uniform", args=(array[0], array[-1] - array[0]), N=nsegments
    )
    kstest_pass = kstest_result.pvalue > 1 - alpha

    if print_test_data:
        data = [
            [
                "chi squared",
                chi_squared_result.statistic,
                chi_squared_result.pvalue,
                str(chi_squared_pass),
            ],
            [
                "kolmogorov-smirnov",
                kstest_result.statistic,
                kstest_result.pvalue,
                str(kstest_pass),
            ],
        ]
        headers = ["test statistic", "p value", "test pass"]
        print(tabulate(data, headers=headers))

    if show_plot:
        plt.show()

    if chi_squared_pass and kstest_pass:
        return True

    return False
