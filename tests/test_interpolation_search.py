import unittest

from distribution_search.interpolation_search import interpolation_search

class TestInterpolationSearch(unittest.TestCase):

    # Returns correct index
    def test_get_index_of_element(self):
        array = [1, 2, 3, 4]
        for element in array:
            with self.subTest(element=element):
                idx = element - 1
                self.assertEqual(interpolation_search(array, element), idx)

    def test_element_at_first_index(self):
        array = [1, 2, 3, 4]
        element = 1
        self.assertEqual(interpolation_search(array, element), 0)

    def test_element_at_last_index(self):
        array = [1, 2, 3, 4]
        element = 4
        self.assertEqual(interpolation_search(array, element), 3)

    def test_len_1_list(self):
        array = [1]
        element = 1
        self.assertEqual(interpolation_search(array, element), 0)
    
    def test_len_1_list_element_not_in_list(self):
        array = [1]
        element = 2
        self.assertRaises(ValueError, interpolation_search, array, element)
    
    def test_get_index_of_first_occurance(self):
        array = [1, 2, 2, 3, 4]
        element = 2
        self.assertEqual(interpolation_search(array, element), 1)

    def test_get_index_of_first_occurance_all_elements_same(self):
        array = [1] * 4
        element = 1
        self.assertEqual(interpolation_search(array, element), 0)

    def test_get_index_of_first_occurance_all_elements_zero(self):
        array = [0] * 4
        element = 0
        self.assertEqual(interpolation_search(array, element), 0)

    def test_get_index_in_large_list(self):
        array = list(range(0, 100000000))   # 100 million
        element = 50512546
        self.assertEqual(interpolation_search(array, element), element)
    
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




    
