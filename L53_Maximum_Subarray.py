# Input:
# A list of numbers

# Output:
# An interger, which is the largest sum of the subarray

# Solution:
# Set both current sum and max sum to be the first number in the list.
# Iterate over the list from the second number.

# If the current sum is larger than the sum of current number and current sum,
# we keep the current sum;
# Otherwise, current number is updated.

# At the end, we compare those current sums and get the max sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)
        return max_sum
    
# Time complexity: O(n)
# Space complexity: O(1)