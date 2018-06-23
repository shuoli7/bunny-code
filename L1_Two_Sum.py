# Input 
# List of numbers, target as an integer

# Output 
# List of indexes whose corresponding integers sum up to the target

# Solution
# To solve the problem, apply data structure "dictionary" 
# to store integer and its index as a key-value pair.
# During the list iteration, we check if target - current number is already in the dict
# If it is, we find the answer.
# If not, we store the current number and index in the dict for thr next round checking

# Clarification
# Can I assume there is a unique combination of two integers or multiple solution?
# In that case, what should we do? 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # First, check the boundary cases
        res = []
        if not nums:
            return res
        
        # Creat a dictionary to store key value pair
        dict = {}

        # Iterate over the list of given nums
        for i in range(len(nums)): 
            if target - nums[i] in dict:
                res.append(dict[target - nums[i]])
                res.append(i)
                return res     
            dict[nums[i]] = i # If target - current number not in the dict, we store key value pair for further check 

# Time complexity: O(n)
# Space complexity: O(n)