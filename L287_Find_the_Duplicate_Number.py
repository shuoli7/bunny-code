# Input:
# A list of nums containing n + 1 integers
# where each integer is between 1 and n (inclusive)

# Output:
# An integer, the duplicate number.

# Solution 1:
# Binary Search
# As all these integers are between 1 and n,
# we will solve this problem with binary search, first we initiate min to be 1,
# max to be len(nums) - 1, and find the middle.

# We count the elements falling in the range[minimum, mid].
# If the count is larger than the capacity of this sub-range,
# it means the duplicate number is in this sub-range.
# So, we set maximum to be mid - 1

# Otherwise, the duplicate number is in the other half sub-range.
# So, we set minimum to be mid + 1

# We keep doing binary search over the input list until minmum is larger than maximum.
# At this time, the duplicate number is the minimum.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = 1
        maximum = len(nums) - 1
        
        while minimum <= maximum:
            mid = int(minimum + (maximum - minimum) / 2)
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                maximum = mid - 1
            else:
                minimum = mid + 1
        return minimum

# Time complexity: O(nlogn)
# Space complexity: O(1)