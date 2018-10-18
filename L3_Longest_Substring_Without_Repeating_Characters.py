# 3. Longest Substring Without Repeating Characters
# Given two strings s("the searching string"), and t("the text"), find the first occurrence of s in t.


# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a sub

# Sliding window method
# 使用字典保存每个字符第一次出现的位置。

# 当right向后遍历的过程中，如果这个字符在字典中，说明这个字符在前面出现过
# 即这个区间已经不是题目要求的不含重复字符的区间了，因此，需要移动left。

# 移动left到哪里呢？有个快速的方法，那就是移动到right字符在字典中出现的位置的下一个位置。

# 无论如何都会使用right更新字典，另外记录最大区间长度即为所求。

# 注意，left更新的时候需要保留最大（最右）的位置。举例说明：

# 对于abba，当right指向最后的a的时候，left指向的是字典中保留的有第一个位置的a，如果不对此进行判断的话，left会移动到第一个字符b。

# left一定是向右移动的，不可能撤回到已经移动过的位置。

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        maxLength = 0
        usedChar = {}
        
        for right in range(len(s)):
            
            # If the letter in the substring repeat, 
            # then the repeated letter is the start of the next substring.
            if s[right] in usedChar: 
                left = max(left, usedChar[s[right]] + 1)
            
            else:
                maxLength = max(maxLength, right - left + 1)   
                
            usedChar[s[right]] = right

        return maxLength
        
# time : O(n)
# space : O(n)
