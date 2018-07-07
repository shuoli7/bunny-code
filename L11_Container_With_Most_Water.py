# Input: 
# A list of non-negative integers, represent the height of vertical lines

# Output:
# An interger, which means the maximum water the container can hold
# The container is constructed by any two lines out of all vertical lines.

# Solution:

# To caculate the maximum water area that the container can hold,
# we multiply height of the container by the length of the container.
# Height of the contaier should be the shorter one of two lines,
# length of the container should be the distance between two lines.

# To solve this problem, we use two pointers 'left' and 'right' to iterate over the list simultaneously.
# Pointer left starts from first line in the list, while pointer right starts from last one.

# At each iteration, we caculate the container area between current left line and right line,
# and then compare the current area with the current maximum area containing water.

# Then, we compare the height of current left line and right line.

# If the left line is shorter than the right line, we move the left pointer to the next line;
# otherwise, we move the right pointer to the previous line.
# Then, we compute and get the max water area in another iteration.

# While left pointer meets the right pointer, the loop ends. 
# Then we can get the maximum water the container holds.

"""
# Exceeds time limit
class Solution(object):
    def maxArea(self, height):

        max_water = 0
  
        for i in range(len(height) - 1):
            for j in range(i, len(height)):
                max_water =max(min(height[i], height[j]) * (j - i), max_water) 
        return max_water
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
    
# Time complexity: O(n)
# Space complexity: O(1)