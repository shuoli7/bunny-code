# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
# To solve this problem, we use the recursive method.

# We have 3 base cases for the recursion.
# If both nodes equal to None, we return True.
# If one node is None and the other is not, we return False.
# If both nodes exist, however, they have different values, we return False.

# If all above cases are not met, we call this isSameTree function itself
# to compare left nodes of these two binary tree, and right nodes of these two binary tree.
# Only if all left nodes are equal, and all right nodes are equal, we can say the two trees are same.

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if p and not q:
            return False
        
        if q and not p:
            return False
        
        if p and q and p.val != q.val:
            return False
        
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
# Time complexity: O(n)
# Space complexity: O(1)