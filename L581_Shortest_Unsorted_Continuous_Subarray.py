# Input:
# A list of integers

# Output:
# An integer, which represents the length of shortest subarray.
# if we sort this subarray in ascending order, then the whole array will be sorted too.

# Solution 1:

# If the input array is in an ascending order, then each number should be the current max
# when we iterate from left to right.
# Also, each number should be the current minimum when we iterate from right to left.

# To solve this problem, first we create two variables represent the current max
# and current min respectively.

# Iterate over the list from left to right first, and find the last time that the current number 
# is not equal to the current max. Then the index is the end point of the subarray.

# Next, Iterate over the list from right to left, and find the last time that the current number 
# is not equal to the current min. Then the index is the start point of the subarray.

# At the end, the length of the subarray is the distance between its staring point and ending point.

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        max_num = nums[0]
        min_num = nums[len(nums) - 1]
        
        for i in range(len(nums)):
            max_num = max(max_num , nums[i])
            if nums[i] != max_num:
                end = i
                
        for j in reversed(range(len(nums))) :
            min_num = min(min_num , nums[j])
            if nums[j] != min_num:
                start = j
                
        if start == end: # that means the given list is already sorted.
            return 0
        else:
            return end - start + 1

# Time complexity: O(n)
# Space complexity: O(1)

# Solution 2:

# To find length of the subarray, we need to find its staring point and ending point.

# Iterate over the input list from left to right.
# The first number that is larger than the next one might be the starting point.

# Then, iterate over the list reversely.
# The number that is smaller than the previous one might be the ending point.

# Next, we want to check whether all numbers in the left of the subarray are less than
# the minimum number in the subarray.
# If not, the starting point of the subarray will move to the smaller number in the left.

# Similarly, if the number in the right of the subarray is larger than the max number
# in the subarray, the ending point will move to the larger number in the right. 

# At the end, the length of the subarray is the distance between its staring point and ending point.

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1
        
        while j > 0 and nums[j] >= nums[j - 1]:
            j -= 1
                
        if i == len(nums) - 1 and j == 0:
            return 0
        
        temp = nums[i:j + 1]
        min_temp = min(temp)
        max_temp = max(temp)
        
        while i > 0 and nums[i - 1] > min_temp:
            i -= 1
        while j < len(nums) - 1 and nums[j + 1] < max_temp:
            j += 1
        
        return j - i + 1

# Time complexity: O(n)
# Space complexity: O(1)