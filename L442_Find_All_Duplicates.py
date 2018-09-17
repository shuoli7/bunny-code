# The idea is we want to take advantage of the fact that the numbers
# in the given list are between 1 and n. 

# We marking elements at certain indexes "negative".
# we can see whether or not something has been visited by using its 'sign'
# as a boolean flag.
# If we have already seen something and are visiting it again,
# The sign will become "positve"
# that means it must have appeared twice, so we add it to the output.

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            idx = abs(num) - 1  
            nums[idx] *= -1
            if nums[idx] > 0:   
                res.append(idx + 1)
        return res

# Time: O(n)
# Space: O(1)