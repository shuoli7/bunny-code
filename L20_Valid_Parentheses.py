# Input: A string containing just brackets

# Output: A boolean True or False
# Return True if open brackets are closed by the same type of brackets in the correct order.

# Solution:
# Use a dictionary to store right bracket in key 
# and left bracket of the same type in value

# Iterate over the string.
# If the character is in the value, which means it is a left bracket,
# store it in the stack

# If the character is not in the value, which means it is a right bracket,
# if it is in a pair with the latest left bracket, or the current stack is empty,
# it means that it is not a valid parentheses. Return False.

# At the end, if the stack is empty, it means all parentheses are valid. Then return True.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {")": "(",
              "}": "{",
              "]": "["}
        for c in s:
            if c in dic.values():
                stack.append(c)
            else:
                if not stack or dic[c] != stack.pop():
                    return False
        return stack == []
                
# Time complexity: O(n)                
# Space complexity: O(1)