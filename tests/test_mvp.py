import unittest

from distribution_search.mvp import get_index

class TestGetIndex(unittest.TestCase):

    def test_basic(self):
        array = [1, 2, 3, 4]
        element = 3
        self.assertEqual(get_index(array, element, array[0], array[-1]), 2)

    def test_element_less_than_minimum(self):
        array = [1, 2, 3, 4]
        element = 0
        self.assertRaises(ValueError, get_index, array, element, array[0], array[-1])

    def test_element_more_than_maximum(self):
        array = [1, 2, 3, 4]
        element = 5
        self.assertRaises(ValueError, get_index, array, element, array[0], array[-1])

    def test_element_not_in_array(self):
        array = [1, 2, 3, 4]
        element = 3.5
        self.assertRaises(ValueError, get_index, array, element, array[0], array[-1])
    
    def test_get_index_of_first_occurance(self):
        array = [1, 2, 2, 3, 4]
        element = 2
        self.assertEqual(get_index(array, element, array[0], array[-1]), 1)


    
