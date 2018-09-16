# Input:
# An unsorted list of integers,
# and another integer k

# Output:
# An integer, which is the kth largest element in the array

# Solution 1:
# To solve this problem, 
# we can sort the list in ascending order first.
# Then the kth largest element is located at (len(nums) - k) index.

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_list = sorted(nums)
        return sorted_list[len(nums) - k]
# Time complexity: O(nlogn)
# Space comlexity: O(1)

# Solution 2 : 
# Divide and conquer / Quick select

# To solve this problem, we pick the first number in the input list as the pivot, 

# Then, iterate over the list. 
# Store larger numbers in list_l, and smaller numbers in list_s.

# If k is smaller than or equal to the length of list_l,
# it means the kth largest number is in the list_l.
# So we search in the list_l;

# If k is larger than the diff between length of input list and length of list_l,
# it means the kth largest number is in the list_s.
# So we search in the list_s;

# Else, the kth largest number is exactly the pivot.
# Return pivot.

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        
        list_l = []
        list_s = []
        pivot = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > pivot:
                list_l.append(nums[i])    
            elif nums[i] < pivot:
                list_s.append(nums[i])
            else:
                continue
        if k <= len(list_l): # it is in the list of large elements
            return self.findKthLargest(list_l, k)
        elif k > len(nums) - len(list_s): # it is in the list of small elements
            return self.findKthLargest(list_s, k - (len(nums) - len(list_s)))
        else:
            return pivot
        
# Time complexity: O(n)
# Space complexity: O(n)

# Solution 3:
from heapq import *
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1
        
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:
                heappush(heap, nums[i])
            else:
                if heap[0] < nums[i]:
                    heapreplace(heap, nums[i])
        return heap[0]

# Time complexity: O(k + (n-k)logk)
# Space complexity: O(n)

# Solution 4:
from heapq import *
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]

# Time complexity: O(k + (n-k)logk)
# Space complexity: O(n)