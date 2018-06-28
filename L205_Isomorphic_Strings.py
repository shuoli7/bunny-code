# Input: Two strings

# Output: A boolean value, True if two strings are isomorphic, False if not.
# Isomorphic means two strings have same structures, such as, abb and bcc.

# Solution:
# Here I use two maps to store s->t mapping and t->s mapping
# Loop over the string s, in each iteration, we get a pair of numbers s[i], t[i].

# If both numbers don't exist in the key set of the two maps,
# we add s->t mapping and t->s mapping to the two maps respectively.

# If only one of them existed in the key set of map, the other is not, return False.

# If both of them existed in the map, but the mapping is wrong, 
# for example map1[s[i]] != t[i], then return False.

# At the end, if no return False case is hit, then we return True after jumping out of for loop.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Edge case
        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}
        for i in range(len(s)):
            if s[i] not in map1 and t[i] not in map2:
                map1[s[i]] = t[i]
                map2[t[i]] = s[i]
            elif s[i] not in map1: # map1 not contain a, map2 contain b
                return False
            elif t[i] not in map2: # map2 not contain b, map1 contain a
                return False  
            else: # map1 contain a AND map2 contain b
                if map1[s[i]] != t[i] or map2[t[i]] != s[i]:
                    return False
        return True
    
# Time complexity: O(n)
# Space complexity: O(n)