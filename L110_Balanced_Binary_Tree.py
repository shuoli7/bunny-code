# Input:
# A binary tree

# Output:
# A boolean variable. Return true if the tree is height-balanced; Otherwise return false.
# If the depth of the two subtrees of every node never differ by more than 1,
# the tree is a height-balanced binary tree.

# Solution:
# To solve this problem, we will use recursion method.

# The base cases for the recursion is, if root is None, we should return True.

# We define a helper function, which takes root node as arguments.
# We call this helper function inside isBalanced()
# to get the depth of the left subtree and right subtree..

# If the depth of the two subtrees of every node never differ by more than 1,
# We will return True.
# So we call the helper function to compare two subtrees of the root node,
# We also call isBalanced() function itself to compare subtrees of root.left,
# and subtrees of root.right.

# After all functions returned, we can see whether it is a height-balanced binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return abs(self.depth(root.left) - self.depth(root.right)) < 2 and \
        self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0

        return 1 + max(self.depth(root.left), self.depth(root.right))

# Time complexity: O(nlogn)?
# Space complexity: O(h)