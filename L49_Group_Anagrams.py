# Input: A list of strings

# Output: A list of lists, by grouping anagrams to one list

# Solution:
# To solve this problem, I am thinking to use a dictionary to help my implementation.

# Because the output is a list of list, each inner list contains a group of anagrams.
# I will use sorted string as key, and list of all of its anagrams plus itself as the value.

# The reason I use dictionary is because, add key-value pair 
# and retrieve value from dictionary are O(1) actions.

# Loop over the list

# if the sorted string is not in the key set of dictionary
# I add sorted string as the key.
# I also add a new list contains this string as the value.

# If the sorted string is in the key set of dictionary
# I add the string in the value list.

# When the iteration ends, add all the value lists to the result list.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dictr = {}
        for string in strs:
            key = str(sorted(string)) # Build-in func sorted() return a sorted list
                                      # which cannot be the key of a dict, 
                                      # so cast the type to string.
            if key not in dictr:
                dictr[key] = [string]
            else:
                dictr[key].append(string)

        for value in dictr.values():
            res.append(value)
        return res

# Time complexity: O(nmlog(m)) # n is the length of the list of strings; 
                               # m is the average length of a string, 
                               # time for sorting each string is mlog(m).
# Space complexity: O(nm)