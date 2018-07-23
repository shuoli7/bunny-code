# Input:
# A binary tree and an integer, which is a target sum of node values in a root-to-leaf path.

# Output:
# A list, which includes all posibilities of root-to-leaf path whose sum is the input integer.

# Solution:
# To solve this problem, we use recursion method.

# We define a helper function, which takes root node, sum, path and result list as arguments.
# We call this helper function inside pathSum().

# In the helper function, there are two base cases for the helper function.

# We first define return condition to check if root is None.
# if it is None, we return because that means there is no future or current node on this path.

# Or, if the root is the last leaf and its value is equal to the target sum integer, it means we find the path.
# So we add the current node to the path list, and then add this path to the result list.

# If this is not the last node of this path, we recursively call helper function to node.left and node.right.
# The target sum for root.left or root.right is sum - root value.
# And the path is previous path + root value.

# After all functions returned, we go back to the top level call in pathSum function,
# we will have all root-to-leaf paths in the result list, so we can return the result list.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.helper(root, sum, res, path)
        return res
    def helper(self, root, sum, res, path):
        if not root:
            return
        if root.val == sum and not root.left and not root.right:
            return res.append(path + [root.val]) # Concatenation
        self.helper(root.left, sum - root.val, res, path + [root.val])
        self.helper(root.right, sum - root.val, res, path + [root.val])

# Time complexity: O(n * h) # n is the average number of tree nodes on each level,
                            # h is the height of the tree.
# Space complexity: O(h) # h is the height of the tree,
