# Author: Matthew Woolley
# Email: matt.wool@live.com.au

import random
import unittest

from search_functions.search_functions import (
    linear_search,
    jump_search,
    binary_search,
    exponential_search,
    interpolation_search,
)

SEARCH_FUNCS = [
    linear_search,
    jump_search,
    binary_search,
    exponential_search,
    interpolation_search,
]


def _run_against_all_search_functions(self, array, element):
    for search_func in SEARCH_FUNCS:
        correct_idx = array.index(element)
        with self.subTest(search_func=search_func):
            args = (array, element)
            if search_func.__name__ == "jump_search":
                args += (4,)  # jump_len = 4
            self.assertEqual(search_func(*args), correct_idx)


def _raise_value_error_for_all_search_functions(self, array, element):
    for search_func in SEARCH_FUNCS:
        with self.subTest(search_func=search_func):
            args = (array, element)
            if search_func.__name__ == "jump_search":
                args += (4,)  # jump_len = 4
            self.assertRaises(ValueError, search_func, *args)


class TestInterpolationSearch(unittest.TestCase):
    def test_randomised_lists(self):
        random.seed(100)  # Generate the same random numbers every time
        for _ in range(1000):  # Conduct 1000 tests
            len_list = random.randint(1, 100)
            array = [random.randint(-100, 100) for _ in range(len_list)]
            array.sort()
            element = random.choice(array)
            with self.subTest(array=array, element=element):
                _run_against_all_search_functions(self, array, element)

    def test_element_at_middle_index(self):
        array = [1, 2, 3, 4]
        element = 2
        _run_against_all_search_functions(self, array, element)

    def test_element_at_first_index(self):
        array = [1, 2, 3, 4]
        element = 1
        _run_against_all_search_functions(self, array, element)

    def test_element_at_last_index(self):
        array = [1, 2, 3, 4]
        element = 4
        _run_against_all_search_functions(self, array, element)

    def test_len_1_list(self):
        array = [1]
        element = 1
        _run_against_all_search_functions(self, array, element)

    def test_get_index_of_first_occurance(self):
        array = [1, 2, 2, 3, 4]
        element = 2
        _run_against_all_search_functions(self, array, element)

    def test_get_index_of_first_occurance_all_elements_same(self):
        array = [1, 1, 1, 1]
        element = 1
        _run_against_all_search_functions(self, array, element)

    def test_get_index_in_large_list(self):
        array = list(range(0, 100000000))  # 100 million
        element = 50512546
        _run_against_all_search_functions(self, array, element)

    def test_positive_and_negative_elements(self):
        array = [-2, -1, 3, 6]
        element = -1
        _run_against_all_search_functions(self, array, element)

    def test_all_negative_elements(self):
        array = [-10, -3, -2, -1]
        element = -2
        _run_against_all_search_functions(self, array, element)

    # Raises error
    def test_empty_list_raises_error(self):
        array = []
        element = 2
        _raise_value_error_for_all_search_functions(self, array, element)

    def test_element_less_than_minimum_raises_error(self):
        array = [1, 2, 3, 4]
        element = 0
        _raise_value_error_for_all_search_functions(self, array, element)

    def test_element_more_than_maximum_raises_error(self):
        array = [1, 2, 3, 4]
        element = 5
        _raise_value_error_for_all_search_functions(self, array, element)

    def test_element_between_elements_raises_error(self):
        array = [1, 2, 3, 4]
        element = 3.5
        _raise_value_error_for_all_search_functions(self, array, element)

    def test_len_1_list_element_not_in_list(self):
        array = [1]
        element = 2
        _raise_value_error_for_all_search_functions(self, array, element)
