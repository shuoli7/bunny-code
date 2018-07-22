# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
# To solve this problem, we use the recursive method.

# First, we have 3 return condition checks
# If both nodes equal to None, we return True.
# If one node is None and the other is not, we return False.
# If both nodes exist, however, they have different values, we return False.

# If all the above cases are not met, we recursively call isSameTree on left nodes
# and also recursively call is SameTree on right nodes. 
# We return the AND logic of them.

# Imagine if return false condition is hit in any level, 
# false will be returned back to the top level eventually 
# such that we will know these two trees are not exactly the same.

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
# Time complexity: O(n)
# Space complexity: O(h) # h is the height of tree