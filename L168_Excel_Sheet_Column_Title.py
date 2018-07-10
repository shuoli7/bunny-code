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
# with our logic, 28 % 26 = 2, then we get C for the rightmost letter.
# So we should compensate that by n - 1.

# Then, we can get the current rightmost letter by using build-in python function chr(),
# and add this letter to the left of previous result.

# Next, we should divide n by 26.

# To know why we do that, I will still take the example of 28.
# In the first round, we get the rightmost letter to be 'B'.
# To find the letter in the left of 'B' in the next round,
# we divide n by 26, which means that we right-shift n by 1 step with base 26.
# Now, we get n to be 1. In the next round, we get the corresponding letter to be 'A'.

# After finishing all rounds, we have the string of letters.
# With the example of 28, our final result is 'AB'.

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        
        while n > 0:
            n -= 1 # 
            unit = n % 26 # get right-most letter
            res = chr(ord("A") + unit) + res
            n /= 26 # right-shift n by 1 step with base 26
        return res
            
# Time complexity: O(n)
# Space complexity: O(1) # memory used to store the result should not be counted 