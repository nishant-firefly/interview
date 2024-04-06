import unittest
from static_array import StaticArray  # Assuming StaticArray class is implemented in static_array.py

class TestStaticArray(unittest.TestCase):
    def setUp(self):
        """
        Fixture to create a StaticArray instance with size 5 for each test function.
        """
        self.static_arr = StaticArray(5)

    def test_initialization(self):
        """
        Test the initialization of the static array and check its initial state.
        """
        self.assertEqual(len(self.static_arr), 5)  # Check the length of the array
        self.assertEqual(str(self.static_arr), "[None, None, None, None, None]")  # Check the string representation

    def test_setitem_and_getitem(self):
        """
        Test setting and getting elements in the static array.
        """
        self.static_arr[0] = 10
        self.static_arr[1] = 20
        self.assertEqual(str(self.static_arr), "[10, 20, None, None, None]")  # Check array after setting values
        self.assertEqual(self.static_arr[0], 10)  # Check value at index 0
        self.assertEqual(self.static_arr[1], 20)  # Check value at index 1
        with self.assertRaises(IndexError):
            value = self.static_arr[5]  # Index out of range, should raise IndexError

    def test_len(self):
        """
        Test the length method of the static array.
        """
        self.assertEqual(len(self.static_arr), 5)  # Check initial length
        self.static_arr[0] = 10
        self.static_arr[1] = 20
        self.assertEqual(len(self.static_arr), 5)  # Length should remain unchanged after setting values

    def test_str(self):
        """
        Test the string representation of the static array.
        """
        self.static_arr[0] = 10
        self.static_arr[1] = 20
        self.assertEqual(str(self.static_arr), "[10, 20, None, None, None]")  # Check string representation after setting values

    def test_index_error(self):
        """
        Test index errors in the static array.
        """
        with self.assertRaises(IndexError):
            value = self.static_arr[5]  # Index out of range, should raise IndexError
        with self.assertRaises(IndexError):
            value = self.static_arr[-1]  # Negative index, should raise IndexError

if __name__ == '__main__':
    unittest.main()