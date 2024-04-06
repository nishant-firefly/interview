import unittest
from dynamic_array import DynamicArray  # Assuming DynamicArray class is implemented in dynamic_array.py

class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        """
        Fixture to create a DynamicArray instance for each test function.
        """
        self.dynamic_arr = DynamicArray()

    def test_initialization(self):
        """
        Test the initialization of the dynamic array and check its initial state.
        """
        self.assertEqual(len(self.dynamic_arr), 0)  # Check the length of the array
        self.assertEqual(str(self.dynamic_arr), "[]")  # Check the string representation

    def test_append_and_getitem(self):
        """
        Test appending elements and getting elements from the dynamic array.
        """
        self.dynamic_arr.append(10)
        self.dynamic_arr.append(20)
        self.assertEqual(len(self.dynamic_arr), 2)  # Check length after appending
        self.assertEqual(str(self.dynamic_arr), "[10, 20]")  # Check array after appending
        self.assertEqual(self.dynamic_arr[0], 10)  # Check value at index 0
        self.assertEqual(self.dynamic_arr[1], 20)  # Check value at index 1

    def test_len(self):
        """
        Test the length method of the dynamic array.
        """
        self.assertEqual(len(self.dynamic_arr), 0)  # Check initial length
        self.dynamic_arr.append(10)
        self.dynamic_arr.append(20)
        self.assertEqual(len(self.dynamic_arr), 2)  # Check length after appending

    def test_str(self):
        """
        Test the string representation of the dynamic array.
        """
        self.dynamic_arr.append(10)
        self.dynamic_arr.append(20)
        self.assertEqual(str(self.dynamic_arr), "[10, 20]")  # Check string representation after appending

    def test_index_error(self):
        """
        Test index errors in the dynamic array.
        """
        with self.assertRaises(IndexError):
            value = self.dynamic_arr[0]  # Empty array, should raise IndexError
        self.dynamic_arr.append(10)
        self.dynamic_arr.append(20)
        with self.assertRaises(IndexError):
            value = self.dynamic_arr[5]  # Index out of range, should raise IndexError

if __name__ == '__main__':
    unittest.main()
