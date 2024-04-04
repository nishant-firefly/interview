"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

def is_contains_dulicate(arr):
    temp_arr=[]
    for elem in arr:
        if elem not in temp_arr:
            temp_arr.append(elem)
        else:
            return True
    return False