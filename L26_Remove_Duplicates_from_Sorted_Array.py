# Input: A sorted list of numbers

# Output: The length of the list without duplicate numbers

# Solution:
# To solve theis problem, we will set two pointers.

# First pointer i, we use it to iterate through the list.
# Secont pointer j, we use it to count how many distinct numbers in the list.

# During the iteration, if the current number is different from the previous one,
# set the number whose index is the current count to be this distinct number,
# and increase the count index by one.
# In this way we put all distinct numbers in order.

# At the end, the list without duplicate numbers is the sliced list end at the lndex of count
# we return the length of the sliced list

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case: if the list did not exist or the length is 0, then we return 0.
        if not nums:
            return 0
        
        j = 1 # There are at least one distinct number in the list
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i]:
                nums[j] = nums[i + 1]
                j += 1
        return len(nums[:j]) # or return j

# Time complexity: O(n)
# Space complexity: O(1)