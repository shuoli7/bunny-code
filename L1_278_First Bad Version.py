# Input
# The numer of the versions

# Output
# The number of the first bad version

# Solution
# To find the first bad version quickly, I use binary search. 
# I guess the middle number and eliminate half the remaining numbers every time.

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) / 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l
            
# Time Complexity: O(log(n))
# Space Complexity: O(1)