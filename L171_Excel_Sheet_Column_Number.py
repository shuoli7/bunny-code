# Input: Column title in Excel

# Output: Coresponding column number

# Solution: 
# Iterate the title string from right to left.
# For the letter "A" to "Z", its corresponding value is the distance between
# this letter and "A" plus 1.

# From right to left, the unit values are 26^0, 26^1,...26^(len(string) - 1)

# Multiply the letter value and its unit value in the string, and add them together.

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        length = len(s)
        for i in reversed(range(length)):
            res += (ord(s[i]) - ord("A") + 1) * (26 ** (length - 1 - i)) # ord(), given a string with length 1 or a character, 
                                                                         # output the corresponding unicode number.
        return res

# Optimized solution:    
# Iterate the title string.

# Set the starting result to be zero.

# For the letter "A" to "Z", its corresponding value is the distance 
# between this letter and "A" plus 1.

# In the each iteration, always multiply the previous result by 26
# Then, add the current value to the previous result.

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in s:
            res = res * 26 + ord(i) - ord("A") + 1
        return res

# Time complexity: O(n)
# Space complexity: O(1)