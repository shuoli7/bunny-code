# Input: A list of integers

# Output: A boolean True or False. If there are no duplicates in the list, it's False.
#Else, it is True

# Method 1

# Solution:
# Creat a set to store the number if it is not in the set.
# Iterate over the list. If the number is in the set, return True.

# After finishing all loops, if we never return True, 
# it means that there are no duplicates in the list, then we return False.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_ints = set()
        for num in nums:
            if num not in set_ints:
                set_ints.add(num)
            else:
                return True
        return False
    
# Time complexity: O(n)
# Space complexity: O(n)


# Method 2

# Solution:
# To reduce the scape complexity to be O(1),
# we can sort the list first.

# Then we can compare each number in the list with the previous one.

# If the current number is same as the previous number, return Ture

# After finishing all loops, if we never return True, 
# it means that all the numbers are different in the list, then we return False.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_list = sorted(nums)
        for i in range(1, len(nums)):
            if sorted_list[i] == sorted_list[i - 1]:
                return True
        return False
    
# Time complexity: O(nlogn)
# Space complexity: O(1)