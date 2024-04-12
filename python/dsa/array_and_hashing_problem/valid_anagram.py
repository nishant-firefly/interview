def is_anagram_inefficient(word1, word2):
    """
    Check if two words or phrases are anagrams of each other.
    
    Time Complexity: O(n log n)
    - Sorting the letters of each word/phrase takes O(n log n) time, where n is the total length of both words/phrases.

    Memory Complexity: O(n)
    - Sorting requires additional memory proportional to the length of the words/phrases.
    """

    # Convert both words/phrases to lowercase and remove spaces for comparison
    word1_cleaned = "".join(word1.lower().split())  # Time Complexity: O(n)
    word2_cleaned = "".join(word2.lower().split())  # Time Complexity: O(n)

    # Sort the letters of each cleaned word/phrase and compare them
    sorted_word1 = sorted(word1_cleaned)  # Time Complexity: O(n log n)
    sorted_word2 = sorted(word2_cleaned)  # Time Complexity: O(n log n)

    return sorted_word1 == sorted_word2

    # Total Time Complexity: O(n log n)


def is_anagram(str1, str2):
    # Convert strings to lowercase for case-insensitive comparison
    str1 = str1.lower() # O(n)
    str2 = str2.lower() # O(n)   => 2xO(n)

    # If lengths are different, they can't be anagrams
    if len(str1) != len(str2):
        return False

    # Create dictionaries to store character counts
    count_str1 = {}
    count_str2 = {}

    # Count occurrences of characters in str1 - O(n)
    for char in str1: # 3xO(n)
        count_str1[char] = count_str1.get(char, 0) + 1

    # Count occurrences of characters in str2 - O(n)
    for char in str2: # 4xO(n)
        count_str2[char] = count_str2.get(char, 0) + 1

    # Compare the dictionaries - O(n)
    return count_str1 == count_str2
    # Total time complexity: O(n)


# Test the function
print(is_anagram('listen', 'silent'))  # Output: True
print(is_anagram('hello', 'world'))    # Output: False


# Test the function
print(is_anagram('listen', 'silent'))  # Output: True
print(is_anagram('hello', 'world'))    # Output: False
if __name__=="__main__":
    word1 = "Listen"
    word2 = "Silent"
    print(is_anagram(word1, word2))  # Output: True

    phrase1 = "Clint Eastwood"
    phrase2 = "Old West Action"
    print(is_anagram(phrase1, phrase2))  # Output: True

"""

word1_cleaned = "".join(word1.lower().split())

Time Complexity: O(n)
split() splits the string into words, which takes O(n) time, where n is the length of the word.
lower() converts the string to lowercase, which also takes O(n) time.
join() concatenates the words back into a string, which takes O(n) time as well.
Overall, this line has a time complexity of O(n) due to the operations involved in cleaning the word.
word2_cleaned = "".join(word2.lower().split())

Similar to the previous line, this line also has a time complexity of O(n) for cleaning the second word/phrase.
sorted_word1 = sorted(word1_cleaned)

Time Complexity: O(n log n)
Sorting the letters of a string using sorted() takes O(n log n) time, where n is the length of the string.
This line has a time complexity of O(n log n) due to sorting the letters of the first cleaned word/phrase.
sorted_word2 = sorted(word2_cleaned)

Similar to the previous line, this line also has a time complexity of O(n log n) for sorting the letters of the second cleaned word/phrase.
return sorted_word1 == sorted_word2

Time Complexity: O(n)
Comparing two sorted lists of letters takes O(n) time, where n is the length of the longer list.
This line has a time complexity of O(n) due to comparing the sorted letters of both words/phrases.
Overall, the time complexity of the is_anagram function is dominated by the sorting operations, 
resulting in a time complexity of O(n log n), where n is the total length of both words or phrases. 
The memory complexity is O(n) due to the additional memory required for sorting, which is proportional to the length of the words or phrases.
"""
