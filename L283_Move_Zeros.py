# Input
# A list of numbers

# Output
# No output, because this is a void function.

# Solutions
# To solve this problem, we will set two pointers.

# First pointer i, we use it to iterate through the list.
# Second pointer j, we place it in a position that all the positions left to it are non-zeros.
# We start j = 0.

# During the iteration, if the current number is non-zero, we swap the number with the number pointed by j.
# Then we increment j. 
# In this way, we ensure that non-zero numbers are all left to position j and their orders
# are not changing.

# At the end, we reach a situation that all positions left to j are non-zero, right to j are zeros or maybe nothing.
# Note that, the number at position j could be zero or non-zero, doesn't matter.

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