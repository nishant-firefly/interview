class StaticArray:
    def __init__(self, size):
        """
        Initializes the static array with a specified size.
        
        Time Complexity: O(n) where n is the size of the array
        Memory Allocation: Allocates memory for an array of size 'size'.
        """
        self.size = size
        self.array = [None] * size

    def __getitem__(self, index):
        """
        Accesses an element in the static array by index.

        Time Complexity: O(1)
        Memory Allocation: No additional memory allocation for accessing an element by index.
        """
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        """
        Sets the value of an element in the static array at the specified index.

        Time Complexity: O(1)
        Memory Allocation: No additional memory allocation for setting an element at an index.
        """
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        """
        Returns the size of the static array.

        Time Complexity: O(1)
        Memory Allocation: No additional memory allocation for getting the size of the array.
        """
        return self.size

    def __str__(self):
        """
        Returns a string representation of the static array.

        Time Complexity: O(n) where n is the size of the array
        Memory Allocation: Memory allocation depends on the size of the array when creating the string representation.
        """
        return str(self.array)