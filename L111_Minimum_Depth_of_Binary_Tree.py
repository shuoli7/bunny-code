# Input:
# A binary tree

# Output:
# An integer, which represents minimum depth of the tree.

# Solution:
# To solve this problem, we use recursion method.

# The base cases for the recursion is when root is None.
# This means that the tree is empty, so we should return 0.

# If a node has both left and right child,
# it means that the node has both left child tree and right child tree,
# so we just recursively find the min height of subtree. However.

# if a node has only one whichever subtree, let's say left subtree,
# so we should find the height of the left subtree itself,
# so we use max in this condition.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

# Time complexity: O(n) # n in all nodes in the tree.     
# Space complexity: O(h) # h is the height of tree.      