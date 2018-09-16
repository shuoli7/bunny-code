# Input:
# A binary tree

# Output:
# A boolean True if the tree is a binary search tree; Otherwise, return False.
# Keys of left subtree must be less than the node's key;
# Keys of right subtree must be larger than the node's key;
# Both left and right subtrees must be binary search tree.

# Solution 1: 
# To solve this problem, we can print inorder traversal of the input tree in a list.
# Then, the list of numbers should be in an increasing order.
# So, we iterate over the list. If a number is larger than the next one, we return false.
# At the end of iteration, if we never hit False, we return True.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.inOrderTraversal(root, res)

        for i in range(1, len(res)):
        	if res[i - 1] >= res[i]:
        		return False
        return True

    def inOrderTraversal(self, root, res):
    	if not root:
    		return
    	self.inOrderTraversal(root.left)
    	res.append(root.val)
    	self.inOrderTraversal(root.right)

# Time complexity: O(n)
# Space complexity: O(n)