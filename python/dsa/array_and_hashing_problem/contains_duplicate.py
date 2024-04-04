"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

def is_contains_dulicate(arr):
    """
    Check if an integer array contains any duplicate values.
    
    Time Complexity: O(n)
    - n is the number of elements in the input array 'arr'.
    - In the worst case, the function may need to iterate through all elements to find duplicates.

    Memory Complexity: O(n)
    - Uses a temporary list 'temp_arr' to store unique elements.
    - The size of 'temp_arr' can grow up to the size of 'arr' in the worst case if 'arr' has no duplicates.
    """
    temp_arr = []
    for elem in arr:
        if elem not in temp_arr:  # Checking if the element is already in the list
            temp_arr.append(elem)  # Adding the element to the list if it's not already there
        else:
            return True  # Returning True if a duplicate is found
    return False  # Returning False if no duplicates are found