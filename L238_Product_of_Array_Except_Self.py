# Input:
# A list of integers

# Output:
# An output list, 
# each element represents product of integers at all positions expect current position.

# Solution:
# To solve this problem, we first create an output array and initialize all elements to be 1.

# To compute final result of each element in the output list,
# we maintain a variable called prod,
# which represents the product of numbers in all previous rounds.

# We use two loops.
# In first loop, we iterate nums from left to right.
# In each round, we first update output[i] by multiplying prod,
# then we update prod by multiplying current num in this round.

# In second loop, we reset prod to 1 
# and iterate nums from right to left, in each round we do the same thing.

# In this way, output[i] has product of all numbers in list nums except number at position i.
# We can output the result.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums) # Output array doesn't count for space complexity.
        
        prod = 1
        for i in range(len(nums)):
            output[i] *= prod
            prod *= nums[i]
        
        prod = 1
        for i in reversed(range(len(nums))):
            output[i] *= prod
            prod *= nums[i]
        
        return output

# Time complexity: O(n)
# Space complexity: O(1)