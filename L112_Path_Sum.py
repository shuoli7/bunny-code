# Input:
# A binary tree and an integer, which is a target sum of node values in a root-to-leaf path.

# Output:
# A boolean variable. Return True, if there exist a root-to-leaf path whose sum is the input integer.
# Otherwise, return False.

# Solution:
# To solve this problem, we use recursion method.

# There are two base cases for the recursion.
# First, when root is None, return False.
# Or, if the root is the last leaf and its value is equal to the target sum integer, return True.

# Else, we call the hasPathSum function itself to check left child and right child of the root.
# The target sum for the child node should be sum - root value.
# The reason for doing this is because the sum of root and child nodes should be the input integer.

# After all functions returned, we can find wheather there is a path whose sum is the input interger. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if root.val == sum and not root.left and not root.right:
            return True

        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# Time complexity: O(n)
# Space complexity: O(h) # h is the height of the tree.