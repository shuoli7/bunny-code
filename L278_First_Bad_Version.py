# Input
# The max number of the versions

# Output
# The number of the first bad version

# Solution
# As I only need to find the first bad version, so I decide to use binary search,
# because binary search can help me to cut 50% of searching space, so that I will
# be able to find the first bad version quickly.

# To do that, I compute the the mid position with every round, and check the version
# at mid position is bad or not, based on that I can decide to search right to mid or left to mid
# in next round. When left go pass right, we jump out condition, the first bad version is
# at the position my left pointer point to.

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left)/ 2 # Because left + right can be a very big number that leads to overflow
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left
            
# Time Complexity: O(log(n))
# Space Complexity: O(1)