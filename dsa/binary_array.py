
import bisect
from enum import Enum

sorted_list = [1, 2, 3, 4]
print('''sorted_list = [1, 2, 3, 4]
index = bisect.bisect_left(sorted_list, 3)  # O(log n) time complexity''')
index = bisect.bisect_left(sorted_list, 3)  # O(log n) time complexity


class Order(Enum):
    ASC = 1
    DESC = -1

class Binary:
    def __init__(self, sorted_list, order=Order.ASC):
        self.sorted_list = sorted_list
        self.order = order

    @staticmethod
    def _get_mid(left, right):
        return left + (right - left) // 2

    def _init_indices(self):
        return 0, len(self.sorted_list) - 1

    def binary_search(self, target):
        left, right = self._init_indices()

        while left <= right:
            mid = self._get_mid(left, right)
            mid_val = self.sorted_list[mid]

            if mid_val == target:
                return mid
            elif (self.order == Order.ASC and mid_val < target) or \
                 (self.order == Order.DESC and mid_val > target):
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def binary_search_rotated(self, target):
        left, right = self._init_indices()

        while left <= right:
            mid = self._get_mid(left, right)
            mid_val = self.sorted_list[mid]

            if mid_val == target:
                return mid
            elif self.sorted_list[left] <= mid_val <= self.sorted_list[right]:
                if (self.order == Order.ASC and mid_val < target) or \
                   (self.order == Order.DESC and mid_val > target):
                    left = mid + 1
                else:
                    right = mid - 1
            elif self.sorted_list[left] <= target <= mid_val:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def get_pivot(self):
        left, right = self._init_indices()

        while left < right:
            mid = self._get_mid(left, right)
            mid_val = self.sorted_list[mid]

            if mid_val > self.sorted_list[right]:
                left = mid + 1
            else:
                right = mid

        return left    
if __name__=="__main__":

    Binary([1, 3, 5, 7, 9, 11, 13, 15], order=Order.ASC)

print('''@pytest.fixture
def binary_desc():
    return Binary([15, 13, 11, 9, 7, 5, 3, 1], order=Order.DESC)
"""
      
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
    assert binary_rotated_desc.binary_search_rotated(8) == -1  # Element not found''')
