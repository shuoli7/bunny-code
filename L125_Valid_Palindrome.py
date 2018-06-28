# Input
# A string 

# Output
# A boolean true or false to determine if the input string is a palindrome.

# Clarification
# If the string is empty, is it a valid palindrome?
# Does the input string contain non-alphanumeric chars?

# Solution
# To solve the problem, I use two pointers to check 
# whether the leftmost character is equal to the rightmost character.

# During the comparison, if the two character is not the same, stop and return False
# If two characters are same, we increment left pointer and decrement right pointer 
# until two characters are different or pointers meet.

# At the end, if return false condition is not met, we return true.

class Solution(object):
    def isPalindrome(self, s):
        if not s:
            return True
        i = 0 # Index of the first character
        j = len(s) - 1 # Index of the last character
        while i < j:
            while i < j and not s[i].isalnum(): # if the first character is not an alphanumeric character, we should move to the next character
                i += 1
            while i < j and not s[j].isalnum(): # if the last character is not an alphanumeric character, we should move to the former character
                j -= 1
            if s[i].lower() != s[j].lower(): # Compare the leftmost character and rightmost character, both are in lower case
                return False
            i += 1
            j -= 1
        return True
     
# Time Complexity: O(n)
# Space Complexity: O(1)