# Author: Matthew Woolley
# Email: matt.wool@live.com.au

import random
import unittest

from interpolation_search.interpolation_search import interpolation_search


class TestInterpolationSearch(unittest.TestCase):

    # Returns correct index
    def test_randomised_lists(self):
        random.seed(100)  # Generate the same random numbers every time
        for _ in range(100):  # Conduct 100 tests
            len_list = random.randint(1, 100)
            array = [random.randint(-100, 100) for _ in range(len_list)]
            array.sort()
            element = random.choice(array)
            with self.subTest(array=array, element=element):
                self.assertEqual(
                    interpolation_search(array, element), array.index(element)
                )

    def test_element_at_middle_index(self):
        array = [1, 2, 3, 4]
        element = 3
        self.assertEqual(interpolation_search(array, element), array.index(element))

    def test_element_at_first_index(self):
        array = [1, 2, 3, 4]
        element = 1
        self.assertEqual(interpolation_search(array, element), array.index(element))

    def test_element_at_last_index(self):
        array = [1, 2, 3, 4]
        element = 4
        self.assertEqual(interpolation_search(array, element), array.index(element))

    def test_len_1_list(self):
        array = [1]
        element = 1
        self.assertEqual(interpolation_search(array, element), array.index(element))

    def test_get_index_of_first_occurance(self):
        array = [1, 2, 2, 3, 4]
        element = 2
        self.assertEqual(interpolation_search(array, element), array.index(element))

    def test_get_index_of_first_occurance_all_elements_same(self):
        array = [1] * 4
        element = 1
        self.assertEqual(interpolation_search(array, element), array.index(element))

    def test_get_index_in_large_list(self):
        array = list(range(0, 100000000))  # 100 million
        element = 50512546
        self.assertEqual(interpolation_search(array, element), array.index(element))

    def test_positive_and_negative_elements(self):
        array = [-2, -1, 3, 6]
        element = -1
        self.assertEqual(interpolation_search(array, element), array.index(element))

    def test_all_negative_elements(self):
        array = [-10, -3, -2, -1]
        element = -2
        self.assertEqual(interpolation_search(array, element), array.index(element))

    # Raises error
    def test_empty_list_raises_error(self):
        array = []
        element = 2
        self.assertRaises(ValueError, interpolation_search, array, element)

    def test_element_less_than_minimum_raises_error(self):
        array = [1, 2, 3, 4]
        element = 0
        self.assertRaises(ValueError, interpolation_search, array, element)

    def test_element_more_than_maximum_raises_error(self):
        array = [1, 2, 3, 4]
        element = 5
        self.assertRaises(ValueError, interpolation_search, array, element)

    def test_element_between_elements_raises_error(self):
        array = [1, 2, 3, 4]
        element = 3.5
        self.assertRaises(ValueError, interpolation_search, array, element)

    def test_len_1_list_element_not_in_list(self):
        array = [1]
        element = 2
        self.assertRaises(ValueError, interpolation_search, array, element)
