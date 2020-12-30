import unittest

from distribution_search.interpolation_search import interpolation_search

class TestInterpolationSearch(unittest.TestCase):

    def test_basic(self):
        array = [1, 2, 3, 4]
        element = 3
        self.assertEqual(interpolation_search(array, element), 2)

    def test_element_at_first_index(self):
        array = [1, 2, 3, 4]
        element = 1
        self.assertEqual(interpolation_search(array, element), 0)

    def test_element_at_last_index(self):
        array = [1, 2, 3, 4]
        element = 4
        self.assertEqual(interpolation_search(array, element), 3)

    def test_element_less_than_minimum(self):
        array = [1, 2, 3, 4]
        element = 0
        self.assertRaises(ValueError, interpolation_search, array, element)

    def test_element_bot_in_array_more_than_maximum(self):
        array = [1, 2, 3, 4]
        element = 5
        self.assertRaises(ValueError, interpolation_search, array, element)

    def test_element_not_in_array_between_elements(self):
        array = [1, 2, 3, 4]
        element = 3.5
        self.assertRaises(ValueError, interpolation_search, array, element)
    
    def test_get_index_of_first_occurance(self):
        array = [1, 2, 2, 3, 4]
        element = 2
        self.assertEqual(interpolation_search(array, element), 1)


    
