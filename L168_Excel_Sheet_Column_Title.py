# Input:
# An integer number

# Output:
# A string of letters, which represents corresponding column title in Excel

# Solution:
# To solve this problem, we run a while loop, the loop continue condition is n > 0.
# Generally, we want to find the string of letters from right to left.

# In each round, first, we compute the the distance between right most letter
# and 'A' by take mod 26 on n - 1.

# The reason we do n - 1 is 'A' equals to 1; For example, AB -> 28,
# with our logic, 28 % 26 = 2, we get C, so
# we should compensate that by minus 1 first.

# Then, we can get the letter by using build-in python function chr().

# We add this letter to the left-most position to previous result,
# then we divide n by 26, and go to the next round.

# After finishing all rounds, we have the string of letters.

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        
        while n > 0:
            n -= 1 # right-shift n by 1 step
            unit = n % 26 # get right-most letter
            res = chr(ord("A") + unit) + res
            n /= 26
        return res
            
# Time complexity: O(n)
# Space complexity: O(1)