# Input:
# A binary tree

# Output:
# the lowest common ancestor (LCA) of two given nodes in the tree

# Solution:

# If one of nodes is the root, then, the root is the LCA.
# Else, we look in left and right child.

# If both children returned a node, it means both p and q found, so parent is LCA
# If either one of the chidren returned a node, meaning either p or q found on left or right branch, we return the node found.
# Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is somewhere below node where 'p' was found, so node where 'p' found is LCA

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q:
            return root
        
        left = right = None
     
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right
        
# Time complexity: O(n)
# Space complexity: O(h)