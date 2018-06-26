# Input
# 2 strings, one is called haystack, the other is called needle

# Output
# If needle is the substring of haystack, return the index of the first occurrence of needle in haystack
# or -1 if needle is not part of haystack.

# Solution
# In this problem, we could compare needle with substring of haystack. The substring should have the same length as needle

# Clarification:
# What should we return when needle is an empty string? 

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)
