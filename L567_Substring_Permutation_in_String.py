# 567. Permutation in String

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").

#--------#

# As the order of the both strings do not matter, hashmap is proper to store the substrings.

# 肯定不可能手动全排列的，时间复杂度太高。

# 思想是，使用和s1等长的滑动窗口判断s2在这个窗口内的字符出现个数和s1的字符出现个数是否相等。

# 使用的是一个字典，统计次数就行，比较简单。第一遍的时候是每次切片都去使用Counter，这样的话超时了
# 所以改用了每次增加窗口最右边的元素，删除最左边的元素，
# 如果左边的元素次数已经为0了，需要手动删除这个元素，否则影响字典相等的判断。

# 时间复杂度为O(N)，空间复杂度O(1)。N为s2长度，假设判断两个字典是否相等的时间复杂度是O(1).


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dict_s1 = collections.Counter(s1)
        left, right = 0, len(s1) - 1
        sub_s2 = collections.Counter(s2[left : right])
        while right < len(s2):
            sub_s2[s2[right]] += 1
            if dict_s1 == sub_s2:
                return True
            else:
                sub_s2[s2[left]] -= 1
            if sub_s2[s2[left]] == 0:
                del sub_s2[s2[left]]
            
            left += 1
            right += 1
        return False
                
                
        
            