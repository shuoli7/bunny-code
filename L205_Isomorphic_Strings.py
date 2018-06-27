# Input: Two strings
# Output: Return True if the two strings are isomorphic
# Solution:
# Here I use two maps to store s->t mapping and t->s mapping
# Only when both maps has no key/value pairs, new pair is added to maps.
# If only one of the pair of character exists, then return False.
# If both characters in the pair exists in two dictionaries, but they are not 1-1 relationship,
# then return False
# If all characters in two strings are 1-1 relationship, we will return True.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
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