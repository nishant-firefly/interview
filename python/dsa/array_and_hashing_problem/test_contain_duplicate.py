import pytest
from contains_duplicate import is_contains_dulicate  # Import your function from the module

def test_is_contains_dulicate():
    """
    Test cases for is_contains_duplicate function.
    """
    # Test with an array containing no duplicates
    arr1 = [1, 2, 3, 4, 5]
    assert is_contains_dulicate(arr1) == False

    # Test with an array containing duplicates
    arr2 = [1, 2, 3, 4, 1]
    assert is_contains_dulicate(arr2) == True

    # Test with an empty array
    arr3 = []
    assert is_contains_dulicate(arr3) == False

    # Test with an array containing only one element
    arr4 = [1]
    assert is_contains_dulicate(arr4) == False

    # Test with a large array containing duplicates
    arr5 = [1] * 1000 + [2] * 1000
    assert is_contains_dulicate(arr5) == True

    # Test with a large array containing no duplicates
    arr6 = list(range(1000))
    assert is_contains_dulicate(arr6) == False

    # Test with negative numbers and zero
    arr7 = [-1, 0, 1, -1]
    assert is_contains_dulicate(arr7) == True

    # Test with mixed data types (integers and strings)
    arr8 = [1, 2, 'a', 'b', 1]
    assert is_contains_dulicate(arr8) == True

    # Test with floating point numbers
    arr9 = [1.5, 2.5, 3.5, 1.5]
    assert is_contains_dulicate(arr9) == True

    # Test with None values
    arr10 = [None, None, 1, 2, 3]
    assert is_contains_dulicate(arr10) == True

    # Test with a mix of data types including None
    arr11 = [None, 'a', 1, 'b', 1]
    assert is_contains_dulicate(arr11) == True