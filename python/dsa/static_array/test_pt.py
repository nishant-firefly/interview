import pytest
from static_array import StaticArray  # Assuming StaticArray class is implemented in static_array.py

@pytest.fixture
def static_arr():
    """
    Fixture to create a StaticArray instance with size 5 for each test function.
    """
    return StaticArray(5)

def test_initialization(static_arr):
    """
    Test the initialization of the static array and check its initial state.
    """
    assert len(static_arr) == 5  # Check the length of the array
    assert str(static_arr) == "[None, None, None, None, None]"  # Check the string representation

def test_setitem_and_getitem(static_arr):
    """
    Test setting and getting elements in the static array.
    """
    static_arr[0] = 10
    static_arr[1] = 20
    assert str(static_arr) == "[10, 20, None, None, None]"  # Check array after setting values
    assert static_arr[0] == 10  # Check value at index 0
    assert static_arr[1] == 20  # Check value at index 1
    with pytest.raises(IndexError):
        value = static_arr[5]  # Index out of range, should raise IndexError

def test_len(static_arr):
    """
    Test the length method of the static array.
    """
    assert len(static_arr) == 5  # Check initial length
    static_arr[0] = 10
    static_arr[1] = 20
    assert len(static_arr) == 5  # Length should remain unchanged after setting values

def test_str(static_arr):
    """
    Test the string representation of the static array.
    """
    static_arr[0] = 10
    static_arr[1] = 20
    assert str(static_arr) == "[10, 20, None, None, None]"  # Check string representation after setting values

def test_index_error(static_arr):
    """
    Test index errors in the static array.
    """
    with pytest.raises(IndexError):
        value = static_arr[5]  # Index out of range, should raise IndexError
    with pytest.raises(IndexError):
        value = static_arr[-1]  # Negative index, should raise IndexError
