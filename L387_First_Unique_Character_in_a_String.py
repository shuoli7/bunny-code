# Input: A string
# Output: The first non-repeating character in the string and return it's index. 

# Solution1 (Brute force)-- Time Limit Exceeded 
# Compare each character with followed character in the string to see whether we can find the non-repeating character.
# As soon as we find it, return the index of the character
# If we can not find such character after the iteration over the string, return -1

# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        for i in range(len(s)):
            isExist = True
            for j in range(len(s)):
                if i != j and s[i] == s[j]:
                    isExist = False
                    break
            if isExist:
                return i   
        return -1

# Solution2 (hashmap)
# Create a hashmap with counts
# Loop over the string and check for counts of each character
# if count is 1, then return index; else return -1

# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            d[c] = 1
        
        for i in range(len(s)):
            c = s[i]
            if d[c] == 1:
                return i
        return -1

# Solution3 (unicode)
# Creat a list with the length of 26, representing 26 positions for 26 positions
# Loop over the string, add 1 to its corresponding location if the character shows up
# Loop over the string again, if the character only showed up once, return its index
# If all characters show up more than once, return -1

# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = [0]*26
    
        for i in range(len(s)):
            chars[ord(s[i]) - ord('a')] += 1
    
        for i in range(len(s)):
            if chars[ord(s[i]) - ord('a')] == 1:
                return i
        return -1