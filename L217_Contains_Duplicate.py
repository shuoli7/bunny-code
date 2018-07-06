# Input:
# A list of integers

# Output: 
# A boolean, True if there is duplicates in the list, False if not.

# Method 1

# Solution:
# We create a set to help check duplicates, because put and search actions 
# (due to hashing) for set is a O(1) process.

# Iterate over the list. If the number is in the set, 
# it means there is a duplicate number, return True.

# After finishing all iterations, if we still didn't hit a duplicate, we return False.

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
# To reduce the space complexity to be O(1),
# we can sort the list first.

# Then Iterate over the list.
# compare each number in the list with the previous one.

# If the current number is same as the previous number, 
# it means there is a duplicate number, return Ture

# After finishing all iterations, if we still didn't hit a duplicate, we return False.

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
    
# Time complexity: O(nlogn) # for most of sorting algorithms, including the algorithm behind 
                            # build-in sort function. The average time complexity is O(nlogn),
                            # most of time, the algorithm behind the build-in sort function is quick-sort.
# Space complexity: O(1)