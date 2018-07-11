# Input:
# A sorted list of numbers

# Output:
# An integer, which represents the length of the list without duplicate numbers.

# Solution:
# To solve theis problem, we will set two pointers.

# First pointer i, we use it to iterate through the list.
# Secont pointer j, we use it to count how many distinct numbers in the list.

# Initialize j with 1
# Because if the list is not empty, we should at least have 1 distinct number.

# During the iteration, if the current number is different from the previous one,
# set number at position with index j to be this distinct number,
# and increase the count index j by 1.
# In this way we can make sure that all the numbers left to position j are distinct.

# At the end, we can simply return j,
# because all the numbers left to position j contains one copy of each distinct number.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case: check if the list is empty
        if not nums:
            return 0
        
        j = 1 # There are at least 1 distinct number in the list
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i]:
                nums[j] = nums[i + 1]
                j += 1
        return j

# Time complexity: O(n)
# Space complexity: O(1)