# Input:
# A list of numbers

# Output:
# An interger, which is the largest sum of a continguous subarray

# Solution:
# To solve this problem, I am thinking to use a dynamic programming method.
# Basically I start from solving subproblems, and build up to solving the big problem.

# To do that, first I create two variables for help,
# curr_sum, which represents the current sum of contiguous subarray
# before adding the current number.
# max_sum, which represents the overall max sum of one contiguous subarray so far.

# During my iteration over the given list of numbers, I keep updating these two variables.

# If current number is bigger than the current sum plus current number,
# we set current number to be current_sum,
# because that means curr_num is a negative value.

# Then, we compare curr_sum with max_sum, and set max_sum with the bigger one.

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