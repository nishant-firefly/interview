#####################1 Array and hashing problem 
"""1.1.
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""
from typing import Union, List
Num = Union[int, float]

class DuplicateMatch:
    def __init__(self, array: List[Num]) -> None:
        self.array = array 

    def is_array_contains_duplicate(self) -> bool:
        arary_elements = set() # Not {} it will be considered as dictionary
        for element in (self.array):
            if element in  arary_elements:
                return True
            else:
                arary_elements.add(element) 
        return False
    def print_status(self) -> None: 
        print(f'{self.array} contains duplicates : {self.is_array_contains_duplicate()}')

DuplicateMatch([1,2,3,4,5,1]).print_status()
DuplicateMatch([1,2,3,4,5,]).print_status()


"""1.2.
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

# class Anagram:
#     def __init__(self, str: word1, str:word2) -> None:
#         pass


