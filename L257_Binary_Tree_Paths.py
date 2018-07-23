# Input:
# A binary tree

# Output:
# A list of all root-to-leaf paths

# Solution (Recursion)
# To solve this problem, we use DFS to traverse this tree, and implement with recursion.

# We define a helper function, which takes root node, path and result list as arguments.
# We call this helper function inside binaryTreePaths().

# In the helper function, we first define return condition to check if root is None.
# if it is None, we return because that means there is no future nodes
# on this path including the current position.

# Then, I defined another return condition check if the current node's left and right nodes are euqal to None,
# if that is the case, that means, this is the last node on this path,
# so we should add it to the path string, then add path string to the result list to end traversal on this path.

# If this is not the last node of this path, so should add "->" to the path first to fulfill the format requirement,
# then we recursively call helper function to node.left and node.right.

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
        
# Time complexity: O(n * h) # n is the average number of tree nodes on each level,
                            # h is the height of the tree.
# Space complexity: O(h) # h is the height of the tree,
                         # we maintain a path during recursion,
                         # so O(h) is due to either the space for maintaining this path or call stack during recursion.       