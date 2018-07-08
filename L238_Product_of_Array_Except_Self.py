# Input:
# A list of integers

# Output:
# A list of output, each output[i] is the product of all intergers
# in the list except the ith element.

# Solution:
# To get each element in the output,
# we multiply all integers that come before the current integer all the way up,
# and all integers that come after it all the way back.

# We set the output to be an array of ones with same length as the input list.

# Then we initiate a product variable to be one,
# this variable means the product of all numbers before the current number.
# We walk through the input list forward.
# For the output array at any given point, we are going to multiply it by the product.
# And set it to that result.
# The product itself becomes what we are looking at in the nums.
# We multiply on the element in nums.

# Then, we go through the backwards ways and do the same thing.

# Reset the product to be one.
# And we walk through the array from the other way.

# For the output array at any given point, we are going to multiply it by that product.
# And set it to that result.
# The product itself is set to what we are looking at in the nums.
# We multiply on the element in nums.

# At the end of these two iterations, we get the output we want.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        
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
# Space complexity: O(1) # The output array has the same length as the input array.