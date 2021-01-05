"""
-----------------------------
Author: Matthew Woolley
Email: matt.wool@live.com.au
-----------------------------

Unittests for array format checking functions
"""
import unittest
from tools.check_array_format import is_array_sorted, are_all_elements_same_type, is_array_correct_format, is_array_correct_type, is_array_uniform

class TestIsArrayCorrectType(unittest.TestCase):

    def test_correct_type(self):
        array = []  # type: list
        array_type = list
        self.assertTrue(is_array_correct_type(array, array_type))

    def test_incorrect_type(self):
        array = {}  # type: dict
        array_type = list
        self.assertFalse(is_array_correct_type(array, array_type))


class TestIsArraySorted(unittest.TestCase):
    def test_array_is_sorted(self):
        array = [1, 2, 3, 4]
        self.assertTrue(is_array_sorted(array))

    def test_array_is_not_sorted(self):
        array = [1, 3, 2, 4]
        self.assertFalse(is_array_sorted(array))

    def test_array_len_1_is_sorted(self):
        array = [1]
        self.assertTrue(is_array_sorted(array))

    def test_empty_array_is_sorted(self):
        array = []
        self.assertTrue(is_array_sorted(array))

class TestAreAllElementsSameType(unittest.TestCase):

    def test_all_elements_same(self):
        array = [1, 2, 3, 4]
        el_type = int
        self.assertTrue(are_all_elements_same_type(array, el_type))
    
    def test_one_element_different(self):
        array = [1, 2, 3.0, 4]
        el_type = int
        self.assertFalse(are_all_elements_same_type(array, el_type))

    def test_multiple_elements_different(self):
        array = ["drax", 2, 3.0, 4]
        el_type = int
        self.assertFalse(are_all_elements_same_type(array, el_type))

    def test_all_elements_different(self):
        array = ["drax", 2.0, 3.0, "gamora"]
        el_type = int
        self.assertFalse(are_all_elements_same_type(array, el_type))

    def test_empty_list(self):

        array = []
        el_type = int
        self.assertTrue(are_all_elements_same_type(array, el_type))

class TestIsArrayUniform(unittest.TestCase):

    def test_uniform_list(self):
        array = list(range(100))
        self.assertTrue(is_array_uniform(array))

    def test_non_uniform_list(self):
        array = [1, 2, 2, 2, 2, 3, 3, 3, 5, 9, 20]
        self.assertFalse(is_array_uniform(array))

    def test_alpha_low(self):   # More stringent
        array = [1, 3, 5, 6, 9]
        alpha = 0.01
        self.assertFalse(is_array_uniform(array, alpha=alpha))

    def test_alpha_high(self):  # Less stringent
        array = [1, 3, 5, 6, 9]
        alpha = 0.5
        self.assertTrue(is_array_uniform(array, alpha=alpha))

    def test_alpha_out_of_bounds(self):
        array = [1, 2, 3, 4]
        for alpha in [-1.0, 1.5]:
            with self.subTest(alpha=alpha):
                self.assertRaises(ValueError, is_array_uniform, array, alpha)



