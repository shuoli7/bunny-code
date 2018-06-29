# Input: A number

# Output: A string of letters, which represents corresponding column title in Excel

# Solution: Basically, it is to transform Decimal system to Hexadecimal.

# First, we get the reminder of (the given number - 1) divided by 26.
# Then, the reminder is the distance between A and the right most letter in the output.
# We can transform the reminder to a letter by built-in Python function, "Chr".

# Then, we divided the number by 26, and follow the above steps again.
# Everytime we get a new letter, we put it in the left of the current result.
# We stop until n is zero. At this moment, we get the string of letters
# which represents the input number.

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        
        while n > 0:
            n -= 1
            unit = n % 26
            res = chr(ord("A") + unit) + res
            n /= 26
        return res
            
# Time complexity: O(n)
# Space complexity: O(n)