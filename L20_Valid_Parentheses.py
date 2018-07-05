# Input: 
# A string containing just brackets, {}, [], ().

# Output: 
# A boolean, True if open brackets are closed by the same type of brackets in the correct order.
# False if not.

# Solution:
# Use a dictionary to store right bracket in key 
# and left bracket of the same type in value

# The reason behind this is, it helps me implement comparison condition later,
# it make codes more clean and retrieve information from dict is a O(1) action,
# so it won't give me penalty on time.

# Iterate over the string.
# If the current char is in the dictionary value set, it means the current char is 
# a left bracket, so we store it in the stack

# If the character is not in the dictionary value set, which means it is a right bracket,
# if the current right bracket is not in a pair with the left bracket on stack top,
# or the current stack is empty at this time,
# then, it means that it is not a valid parentheses. We return False.

# At the end, if the stack is empty, it means all parentheses are matched up. We return True.
# Otherwise, it means there is left-side bracket left in the stack, we return False.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {")" : "(",
               "}" : "{",
               "]" : "["}
        for char in s:
            if char in dic.values(): # If char is a left-side bracket
                stack.append(char)
            else:
                if not stack or dic[char] != stack.pop():
                    return False
        return stack == [] # If stack is empty, means all parenthesis perfectly matched up, 
                           # we return True.
                           # Otherwise, it means there is left-side bracket left in the stack, 
                           # we return False.
                
# Time complexity: O(n)                
# Space complexity: O(1)