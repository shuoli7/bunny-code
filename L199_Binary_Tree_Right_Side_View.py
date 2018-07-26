# Input:
# A binary tree

# Output
# A list of rightmost nodes from top to bottom

# Solution
# To solve this problem we use recursion method.

# The base cases for the recursion is, if root is None, we should return [].

# We define a helper function, which takes root node, res, depth as arguments.
# We call this helper function inside rightSideView() to get the res.

# We initiate teh depth of the tree to be 0.
# If the depth of the tree is same as the res length, we add the node value to the res.

# Then we call the helper function to print the node.right in the following levels.
# If there is no node.right in the level, we will print node.left instead

# After all functions returned, we can get the list with the rightmost nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        depth = 0
        self.helper(root, res, depth)
        return res
    
    def helper(self, node, res, depth):
        if not node:
            return []
        if depth == len(res):
            res.append(node.val)
        self.helper(node.right, res, depth + 1)
        self.helper(node.left, res, depth + 1)
    
# Time complexity: O(n)
# Space complexity: O(h) # h is the height of the tree