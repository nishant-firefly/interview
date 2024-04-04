import pytest
from dynamic_array import DynamicArray  # Assuming DynamicArray class is implemented in dynamic_array.py

@pytest.fixture
def dynamic_arr():
    """
    Fixture to create a DynamicArray instance for each test function.
    """
    return DynamicArray()

def test_initialization(dynamic_arr):
    """
    Test the initialization of the dynamic array and check its initial state.
    """
    assert len(dynamic_arr) == 0  # Check the length of the array
    assert str(dynamic_arr) == "[]"  # Check the string representation

def test_append_and_getitem(dynamic_arr):
    """
    Test appending elements and getting elements from the dynamic array.
    """
    dynamic_arr.append(10)
    dynamic_arr.append(20)
    assert len(dynamic_arr) == 2  # Check length after appending
    assert str(dynamic_arr) == "[10, 20]"  # Check array after appending
    assert dynamic_arr[0] == 10  # Check value at index 0
    assert dynamic_arr[1] == 20  # Check value at index 1

def test_len(dynamic_arr):
    """
    Test the length method of the dynamic array.
    """
    assert len(dynamic_arr) == 0  # Check initial length
    dynamic_arr.append(10)
    dynamic_arr.append(20)
    assert len(dynamic_arr) == 2  # Check length after appending

def test_str(dynamic_arr):
    """
    Test the string representation of the dynamic array.
    """
    dynamic_arr.append(10)
    dynamic_arr.append(20)
    assert str(dynamic_arr) == "[10, 20]"  # Check string representation after appending

def test_index_error(dynamic_arr):
    """
    Test index errors in the dynamic array.
    """
    with pytest.raises(IndexError):
        value = dynamic_arr[0]  # Empty array, should raise IndexError
    dynamic_arr.append(10)
    dynamic_arr.append(20)
    with pytest.raises(IndexError):
        value = dynamic_arr[5]  # Index out of range, should raise IndexError