# Input
# A list of strings

# Output
# The longest common prefix string amongst an array of strings

# Solution
# Use the first string as the benckmark, and compare it with following strings one by one.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        res = ""
        
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

# Time complexity: O(mn)
# Space complexity: O(1)