# Input
# A list of strings

# Output
# The longest common prefix string among a list of strings

# Solution
# We use the first string as the benchmark string, and use a for loop to iterate each char.
# Under this iteration, we have another for loop that iterates the rest list of strings.

# Then we compare and check at the current index position, if char from benchmark string is equal to char from
# other strings.

# If there is a mis-match or current index is over the length of any other string,
# we stop here and return benchmark string sliced at current index position.

# If both for loops end, we still don't meet a return condition. We return benchmark string.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

# Time complexity: O(mn) # m is length of first string, n is length of the list of strings.
# Space complexity: O(1)