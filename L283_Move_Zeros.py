# Input
# A list of numbers

# Output
# A list of numbers with order changed

# Solutions
# Use two points, one point points to 0, the other point points to the current number. 
# If the current number is not 0, make in-place change on the two numbers.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

# Time complexity: O(n)
# Space complexity: O(1)