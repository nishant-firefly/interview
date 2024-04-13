import pytest
from binary_array import Binary, Order

import pytest

@pytest.fixture
def binary_asc():
    return Binary([1, 3, 5, 7, 9, 11, 13, 15], order=Order.ASC)

@pytest.fixture
def binary_desc():
    return Binary([15, 13, 11, 9, 7, 5, 3, 1], order=Order.DESC)

@pytest.fixture
def binary_rotated_asc():
    return Binary([9, 11, 13, 15, 1, 3, 5, 7], order=Order.ASC)

@pytest.fixture
def binary_rotated_desc():
    return Binary([7, 5, 3, 1, 15, 13, 11, 9], order=Order.DESC)

def test_binary_search_asc(binary_asc):
    assert binary_asc.binary_search(7) == 3  # Element found at index 3
    assert binary_asc.binary_search(10) == -1  # Element not found

def test_binary_search_desc(binary_desc):
    # Update the sorted list to include the element 1
    binary_desc.sorted_list = [15, 13, 11, 9, 7, 5, 3, 1]
    sorted_list = binary_desc.sorted_list  # Get the updated sorted list from the Binary object
    target = 1
    index = binary_desc.binary_search(target)
    assert index != -1, f"Element {target} not found in sorted list {sorted_list}"

def test_binary_search_rotated_asc(binary_rotated_asc):
    assert binary_rotated_asc.binary_search_rotated(11) == 1  # Element found at index 1
    assert binary_rotated_asc.binary_search_rotated(8) == -1  # Element not found

def test_binary_search_rotated_desc(binary_rotated_desc):
    assert binary_rotated_desc.binary_search_rotated(1) == 3  # Element found at index 3
    assert binary_rotated_desc.binary_search_rotated(8) == -1  # Element not found
def test_binary_search_pivot():
    sorted_list = [4, 5, 6, 7, 0, 1, 2]
    binary = Binary(sorted_list)
    assert binary.get_pivot() == 4  # Positive index value for pivot
    assert binary.get_pivot() == 4  # Negative index value for pivot

