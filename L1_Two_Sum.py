# Input is a list of numbers and a target
# Output should be a list of indexes for two integers whose sum is the target
# The data structure I use is dictionary
# store the value of the integer in "key" 
# and corresponding index in "value"

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

        # Interate over the list of given nums
        for i in range(len(nums)): 
            if target - nums[i] in dict: # Check if the difference
            # between the target and current number is in the dictionary
                res.append(dict[target - nums[i]])
                res.append(i)     
            dict[nums[i]] = i # Store key value pair for further check 
        return res

# Time complexity: O(n)
# Space complexity: O(n)