# Input:
# Two strings	
	
# Output:
# If one string is an anagram of another string, return True; 	
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
# First, we create a unicode distance list with length of 26.
# The index here is the unicode distance from current char to 'a'.
# The value at each index is the count of appearance of each character.

# Then we iterate the first string, increment the value at the unicode distance location by 1.

# Next, we iterate the second string, decrement the value at the unicode distance location by 1.

# If the list ends with zeros at all position, return True; Else, return False.	
	
class Solution(object):	
    def isAnagram(self, s, t):	
        """	
        :type s: str	
        :type t: str	
        :rtype: bool	
        """	
        char = [0] * 26
        
        # Increment the frequency of this char by 1
        for c in s:	
            char[ord(c) - ord("a")] += 1
        
        # Decrement the frequency of this char by 1
        for c in t:	
            char[ord(c) - ord("a")] -= 1
            
        # If t is the anagram of s, then all the numbers in the list should be zero. 
        for i in range(26):	
            if char[i] != 0:	
                return False	
        return True	
	
# Time complexity: O(n)	
# Space complexity: O(1) # if all the char in given string is small-case alphabetical char.
                         # If it is, then the helper list has a constant length of 26, 
                         # it is not really growing with n.

# Solution 3:
# if the inputs contain unicode characters, I use a dictionary instead
# because there won't be a fixed size of my helper data structure.
# Add or update info to dict is an O(1) action.

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
                
        # Iterate over t string, subtract frequency of char from the dict. 
        for c in t:
            if c not in dict:
                return False
            else:
                dict[c] -= 1
        
        # If t is the anagram of s, then all the values in the dictionary should be zero. 
        for value in dict.values():
            if value != 0:
                return False
        return True

# Time complexity: O(n) 
# Space complexity: O(n)