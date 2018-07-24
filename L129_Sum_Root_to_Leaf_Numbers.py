# Input:
# Given a binary tree containing digits from 0-9 only,
# each root-to-leaf path could represent a number.

# Output:
# Find the total sum of all root-to-leaf numbers.

# Solution:
# To solve this problem, we use recursion method.

# The base cases for the recursion is when root is None.
# This means that the tree us empty, so we should return 0.

# Or, if the node exists, we should mutiplty the previous root-to-leaf number by 10,
# and add the current node value. Now, we update the root-to-leaf number.

# When there are no left child and right child, we reached the last leaf.
# At the time, we get the root-to-leaf number for one path.
# So we add the number to the res.

# After all functions returned, we can get the sum of all root-to-leaf numbers.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        num = 0
        self.helper(root, num)
        return self.res
    
    def helper(self, node, num):
        if not node:
            return 0
        else:
            num = num * 10 + node.val
            
            if not node.left and not node.right:
                self.res += num
            self.helper(node.left, num)
            self.helper(node.right, num)
            return self.res
        
# Time complexity: O(n) # n in all nodes in the tree.     
# Space complexity: O(h) # h is the height of tree.