# Input: 
# A list of non-negative integers, represents the height of vertical lines

# Output:
# An interger, which means the maximum water the container can hold
# The container is constructed by any two lines out of all vertical lines.

# Solution:

# To solve this problem, I use DP method, break down a complex problem to sub-problems.
# In this particular problem, we keep update max area in each round of iteration.

# To calculate the maximum water area that the container can hold,
# we multiply height of the container by the length of the container.
# Height of the contaier should be the shorter one of two lines,
# length of the container should be the distance between two lines.

# We use two pointers 'left' and 'right' to iterate over the list simultaneously.
# Pointer left starts from first line in the list, while pointer right starts from last one.

# In each round, we calculate the container area between current left line and right line,
# and compare the current area with the current maximum area containing water.

# Then, we compare the height of current left line and right line.
# If the left line is shorter than the right line, we move the left pointer to the next line;
# otherwise, we move the right pointer to the previous line.
# The reason behind this is,
# we can possibly get a bigger max area than previous one in next round.

# Then, we compute and get the max water area in next round.

# While left pointer meets the right pointer, the loop ends. 
# Then we can get the maximum water the container holds.

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