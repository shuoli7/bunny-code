# Input: A string of words seperated by " "
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
        s = s.split()
        if not s:
            return 0
        return len(s[-1])

# Time complexity: O(1)
# Space complexity: O(1)