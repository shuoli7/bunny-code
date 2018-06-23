# Input is a list of numbers and a target; 
# Output should a list of indexes for two integers whose sum is the target
# The data structure I use is hashmap
# store the value of the integer in "key" 
# and coresponding index in "value"

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
        
        # Creat a hashmap to store key value pair
        dict = {}
        # Interate over the list of given nums
        for i in range(len(nums)): # Check before updating the hashmap
            if target - nums[i] in dict: 
                res.append(dict[target - nums[i]])
                res.append(i)     
            dict[nums[i]] = i # Store key value pair into the hashmap
        return res

#Time complexity: O(n)
#Space complexity: O(n)