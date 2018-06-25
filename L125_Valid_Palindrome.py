# Input
# a string 

# Output
# determine if it is a palindrom

# Solution
# To solve the problem, I use two pointers to check 
# whether the leftmost character is equal to the rightmost character
# During the comparison, if the two character is not the same, stop and return False
# If not, the comparison continues until the two pointers meet. 
# If all checks passes, then return True.

# Clarification
# If the string is empty, is it a valid palindrome?

class Solution(object):
    def isPalindrome(self, s):
        if not s:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
     
#Time Complexity: O(n)
#Space Complexity: O(1)
        
        