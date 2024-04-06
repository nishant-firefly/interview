class DynamicArray:
    def __init__(self):
        """
        Initializes the dynamic array as an empty list.
        
        Time Complexity: O(1)
        Memory Allocation: The list is initially empty, so no memory allocation for elements.
        """
        self.array = []

    def append(self, value):
        """
        Appends a new element to the end of the dynamic array.

        Time Complexity: O(1) amortized (amortized constant time)
        Memory Allocation: Python's list automatically handles memory allocation.
        If the underlying array needs resizing (e.g., it reaches capacity), Python allocates a new, larger array 
        (typically double the size of the old array) and copies existing elements to the new array.
        This resizing and copying operation happens occasionally and is amortized O(1) per append operation.
        """
        self.array.append(value)

    def pop(self):
        """
        Removes and returns the last element of the dynamic array.

        Time Complexity: O(1)
        Memory Allocation: No additional memory allocation needed for popping an element.
        """
        return self.array.pop()

    def __getitem__(self, index):
        """
        Accesses an element in the dynamic array by index.

        Time Complexity: O(1)
        Memory Allocation: No memory allocation for accessing an element by index.
        """
        return self.array[index]

    def __len__(self):
        """
        Returns the length of the dynamic array.

        Time Complexity: O(1)
        Memory Allocation: No additional memory allocation for getting the length of the array.
        """
        return len(self.array)

    def __str__(self):
        """
        Returns a string representation of the dynamic array.

        Time Complexity: O(n) where n is the length of the array
        Memory Allocation: Memory allocation depends on the size of the array when creating the string representation.
        """
        return str(self.array)