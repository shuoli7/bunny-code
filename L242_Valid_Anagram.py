# Input: Two strings	
	
# Output: If one string is an anagram of another string, return True; 	
# Otherwise, return False.	
	
# Solution 1:	
# Sort these two strings and compare them.	
	
class Solution(object):	
    def isAnagram(self, s, t):	
        """	
        :type s: str	
        :type t: str	
        :rtype: bool	
        """	
        if sorted(t) == sorted(s):	
            return True	
        return False	
	
# Time complexity: O(nlogn)	
# Space complexity: O(1)	
	
# Solution 2:	
# Create a unicode list with the length of 26.	
# Loop over the first string, count the frenquency of each character	
# and put it at the location based on the character's unicode.	
# Loop over the second string, subtract the frequency of each character.	
# If the list ends with all zeros, return True; Else, return False.	
	
class Solution(object):	
    def isAnagram(self, s, t):	
        """	
        :type s: str	
        :type t: str	
        :rtype: bool	
        """	
        char = [0] * 26
        
        # Add the frenquency of characters in the s string to the list
        for c in s:	
            char[ord(c) - ord("a")] += 1
        
        # Substract the frenquency of characters in the t string from the list
        for c in t:	
            char[ord(c) - ord("a")] -= 1
            
        # If t is the anagram of t, then all the numbers in the list should be zero. 
        for i in range(26):	
            if char[i]!= 0:	
                return False	
        return True	
	
# Time complexity: O(n)	
# Space complexity: O(n)	

# Solution 3:
# if the inputs contain unicode characters, I use a dictionary instead

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        
        # Add the frenquency of characters in the s string to the dictionary
        for c in s:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
                
        # Substract the frenquency of characters in the t string from the list 
        for c in t:
            if c not in dict:
                return False
            else:
                dict[c] -= 1
        
        # If t is the anagram of t, then all the values in the dictionary should be zero. 
        for value in dict.values():
            if value!= 0:
                return False
        return True