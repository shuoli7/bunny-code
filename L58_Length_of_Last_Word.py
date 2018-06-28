# Input: A string of words seperated by space
# Output: The length of the last word

# Solution: 
# Split the string to be a list of words,
# then it is quick to get the length of the last word in the list.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split() # splits string with space by default
        if not s:
            return 0
        return len(s[-1])

# Time complexity: O(n)
# Space complexity: O(1)