# Input:
# A binary tree

# Output:
# A boolean variable. Return True if the tree is symmetric around its center. Otherwise, return False.

# Solution (Recursive)
# To solve this problem, we use recursive method.

# We define a helper function, which takes root.left and root.right as arguments.
# We call the helper function inside.

# In the helper function, we define three return conditions.
# If both left node and right node are None, we return True.
# If left node is None or right node is None, it means we only have one child.
# Then, the tree is not symmetric. So we return False.
# If both childs exists but they have different values, then it is not symmetric. So we return False.

# Else, if both nodes exist, and they have same values,
# then we need continue to compare left child of the left node with the right child of the right node,
# and also compare right child of the left node with the left child of the right node,

# After all functions returned, we go back to the top level call, and return True or False.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left and right and left.val != right.val:
            return False
        else:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
 
# Time complexity: O(n)        
# Space complexity: O(1)