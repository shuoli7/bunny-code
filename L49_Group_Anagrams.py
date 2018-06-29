# Input: A list of strings

# Output: A list of lists, by grouping anagrams to one list

# Solution:
# To solve this problem, I create a dictionary to group those anagrams.

# Loop over the list

# if the sorted string is not in the key set of dictionary
# I store the sorted string into the key list while the string be the value.

# If the sorted string is in the key set of dictionary
# I add the string in the value list.

# when the iteration ends, add all the value list to the result list one by one.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dictr = {}
        for string in strs:
            key = str(sorted(string)) # list can not be the key in a dictionary, so I change it to be a string
            if key not in dictr:
                dictr[key] = [string]
            else:
                dictr[key].append(string)
        for value in dictr.values():
            res.append(value)
        return res

# Time complexity: O(nmlog(m)) # n is the length of the list of strings; m is the length of string, time for sorting each string is mlog(m).
# Space complexity: O(nm)