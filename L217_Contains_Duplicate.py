# Input: A list of integers

# Output: A boolean True or False. If there are no duplicates in the list, it's False.
#Else, it is True

# Solution:
# As list can store duplicates in order, 
# and set stores numbers without duplicates or order,
# the quickest way is to compare the length of the list and its set.

# If they have different length, then they are duplicates, return False.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
    
# Time complexity: O(1)
# Space complexity: O(1)