# Input:
# A string

# Output:
# An integer, which represents the index of first non-repeating char in the string.

# Solution1 (hashmap)
# To solve this problem, we use a dictionary to help implementation.

# Loop over the string,
# I will set each character as the key and its frequency of appearance as value.

# After iteration, I loop over string again using index.
# In each round, I will check if the value for that character in dict is 1.
# If value is 1, we return that index.
# If at the end we still didn't find a key with value 1 in dict, we return -1.

# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for char in s:
            if char in dic.keys():
                dic[char] += 1
            else：
                dic[char] = 1
        
        for i in range(len(s)):
            char = s[i]
            if dic[char] == 1:
                return i
        return -1

# Solution2 (unicode)
# To solve this problem, we create a list with length of 26.

# The index of this list represents the unicode distance from current char to 'a',
# The value of this list represents the frequency of appearance at each position.

# Loop over the string, compute the unicode distance, 
# and increment the value at that position by 1.

# Loop over the string again, if we find value is 1 at certain position, 
# we return the index immediately.

# If at the end, we don't find a position with value 1. We return -1.

# Time complexity: O(n)
# Space complexity: O(1) # If only small-case alphabetical letters are given, 
                         # then we know the size of this fixed sized list is 26.
                         # The length of this list won't increase with
                         # the length of given string. So we can think space is O(1).

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = [0] * 26
    
        for i in range(len(s)):
            chars[ord(s[i]) - ord('a')] += 1
    
        for i in range(len(s)):
            if chars[ord(s[i]) - ord('a')] == 1:
                return i
        return -1

# Solution3 (bruteforce)
# To solve this problem,
# we compare each char with the rest of chars in the string with two nested loops.

# If we don't find a match for certain char, we return index for char in outside loop.
# If we find a match, we continue the outside loop.
# If at the end of two loops, we still didn't hit return index case, we return -1.

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
            is_exist = True
        for j in range(len(s)):
                if i != j and s[i] == s[j]:
                    isExist = False
                    break
            if isExist:
                return i   
        return -1