class Stack:
    def __init__(self):
        """
        Initialize the stack with an empty dynamic array.
        
        Time Complexity: O(1)
        Memory Allocation: O(1)
        """
        self.stack = []

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Time Complexity: O(1)
        Memory Allocation: O(1)
        """
        return len(self.stack) == 0

    def push(self, item):
        """
        Push an item onto the top of the stack.
        
        Time Complexity: O(1) amortized
        Memory Allocation: O(1)
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove and return the item at the top of the stack.
        
        Time Complexity: O(1) amortized
        Memory Allocation: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        
        Time Complexity: O(1)
        Memory Allocation: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.stack[-1]

    def size(self):
        """
        Return the number of items in the stack.
        
        Time Complexity: O(1)
        Memory Allocation: O(1)
        """
        return len(self.stack)

    def __str__(self):
        """
        Return a string representation of the stack.
        
        Time Complexity: O(n)
        Memory Allocation: O(n)
        """
        return str(self.stack)