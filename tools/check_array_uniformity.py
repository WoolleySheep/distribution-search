import matplotlib.pyplot as plt
from scipy.stats import chisquare, kstest
from tabulate import tabulate


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
