# Input:
# A binary tree

# Output:
# A list of all root-to-leaf paths

# Solution (Recursion)
# To solve this problem, we use the recursive method.

# We define a helper function, which takes root node, path and result list as arguments.
# We call this helper function inside binaryTreePaths().

# In the helper function, we first define the return condition to be root equals to None.

# As we need to go all the way down to the last leaf,
# we recursively call helper function to the root.left and root.right
# until we reach the node who has no left child or right child.
# Then we get the last node for the path, and add this path to the result list.

# If the root has left child or right child, we will add this node value to the path.
# Then we recursively call helper function for root.left as well as root.right.

# After all functions returned, we go back to the top level call in binaryTreePaths function,
# we will have all root-to-leaf paths in the result list, so we can return the result list.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        res = []
        path = ""
        self.helper(root, res, path)
        return res
    
    def helper(self, root, res, path):
        if not root:
            return
        if not root.left and not root.right:
            path += str(root.val)
            res.append(path)
        else:
            path += str(root.val) + "->"
            self.helper(root.left, res, path)
            self.helper(root.right, res, path)
        
# Time complexity: O(n)
# Space complexity: O(n)        