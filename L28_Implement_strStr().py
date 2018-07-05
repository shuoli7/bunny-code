# Input
# Two strings, one is called haystack, the other is called needle

# Output
# If needle is the substring of haystack, return the index of the first occurrence of needle in haystack
# or -1 if needle is not part of haystack.

# Solution
# To solve this problem, we first will iterate haystack string from 0 to len(haystack) - len(needle) + 1.
# The reason for that is, the left part of haystack should be at least as long as needle.

# In each iteration, we will compare needle against a substring of haystack sliced by [i:i + len(needle)],
# this substring starts from current position and has the same length as needle string.

# If there is a match, then we find the first appearance of needle as a substring of haystack. 
# We return i as the current position index.

# If after all the iteration, we still cannot find a match, we will return -1.

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
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)
