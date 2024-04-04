import pytest
from stack import Stack  # Assuming Stack class is implemented in stack.py

@pytest.fixture
def empty_stack():
    """
    Fixture to create an empty stack for each test function.
    """
    return Stack()

@pytest.fixture
def filled_stack():
    """
    Fixture to create a filled stack for testing peek, pop, and size methods.
    """
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    return stack

def test_is_empty(empty_stack):
    """
    Test is_empty method for an empty stack.
    """
    assert empty_stack.is_empty() == True

def test_push(empty_stack):
    """
    Test push method to add items to the stack.
    """
    empty_stack.push(10)
    assert empty_stack.size() == 1
    empty_stack.push(20)
    assert empty_stack.size() == 2

def test_pop(filled_stack):
    """
    Test pop method to remove and return items from the stack.
    """
    assert filled_stack.pop() == 30
    assert filled_stack.pop() == 20
    assert filled_stack.size() == 1

def test_peek(filled_stack):
    """
    Test peek method to return the top item without removing it.
    """
    assert filled_stack.peek() == 30
    assert filled_stack.size() == 3  # Size remains unchanged

def test_size(empty_stack, filled_stack):
    """
    Test size method to return the number of items in the stack.
    """
    assert empty_stack.size() == 0
    assert filled_stack.size() == 3

def test_str(empty_stack, filled_stack):
    """
    Test string representation of the stack.
    """
    assert str(empty_stack) == "[]"
    assert str(filled_stack) == "[10, 20, 30]"

def test_pop_empty(empty_stack):
    """
    Test pop method on an empty stack, expecting IndexError.
    """
    with pytest.raises(IndexError):
        empty_stack.pop()

def test_peek_empty(empty_stack):
    """
    Test peek method on an empty stack, expecting IndexError.
    """
    with pytest.raises(IndexError):
        empty_stack.peek()

"""
The __init__ method initializes the stack with an empty dynamic array. Both time complexity and memory allocation are constant (O(1)).
The is_empty method checks if the stack is empty, which takes constant time and memory (O(1)).
The push method adds an item to the top of the stack, with amortized constant time and memory complexity (O(1)).
The pop method removes and returns the top item from the stack, also with amortized constant time and memory complexity (O(1)).
The peek method returns the top item without removing it, taking constant time and memory (O(1)).
The size method returns the number of items in the stack, with constant time and memory complexity (O(1)).
The __str__ method creates a string representation of the stack, which has linear time and memory complexity (O(n)) where n is the number of items in the stack.
"""