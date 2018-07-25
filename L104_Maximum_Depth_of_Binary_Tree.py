# Input:
# A binary tree

# Output:
# An integer, which represents maximum depth of the tree.

# Solution:
# To solve this problem, we use recursion method.

# The base cases for the recursion is when root is None.
# This means that the tree is empty, so we should return 0.

# We recursively call maxDepth function on root.left, and root.right.
# Get the max depth of left sub tree and right sub tree.
# Then the maximum depth of binary tree is the max depth of the subtree plus 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Time complexity: O(n)
# Space complexity: O(h)