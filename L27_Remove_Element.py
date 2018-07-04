# Input
# A list of numbers and a value.

# Output
# The length of new list after deleting all numbers of the input value from the list.

# Solutions
# To solve this problem, we will set two pointers.

# First pointer i, we use it to iterate through the list.
# Second pointer j, we place it in a position that 
# all the positions left to it are not same as the input value.
# We start j = 0.

# During the iteration, if the current number is not same as the input value, 
# we swap the number with the number pointed by j.
# Then we increment j. 
# In this way, we ensure that numbers other than the input value are all left to position j 
# and their orders are not changing.

# At the end, we reach a situation that all positions left to j are not same as the input value, 
# right to j are same as the input value or maybe nothing.
# Then We get the sliced list up to position j.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return len(nums[:j])

# Time complexity: O(n)
# Space complexity: O(1)