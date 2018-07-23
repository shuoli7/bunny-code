# Input:
# A binary tree

# Output:
# An inverted binary tree. Basically, for each node, we swap its left and right nodes.

# Solution (Recursion)
# The base case for the recursion is when root is None, return None.

# If root.left exists, then call the invert function and invert the left subtree.

# If root.right exists, then call the invert function and invert the right subtree.

# If both root.left and root.right exist, then swap them

# After all functions returned, we finish inverting the tree. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.left:
            self.invertTree(root.left)

        if root.right:
            self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

# Time complexity: O(n)
# Space complexity: O(h)