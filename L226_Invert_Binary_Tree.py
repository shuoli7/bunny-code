# Input:
# A binary tree

# Output:
# An inverted binary tree. Basically, for each node, we swap its left and right nodes.

# Solution (Recursion)
# The base case for the recursion is when root is None, return None.

# If root.left exists, then call the invert function and invert the left subtree.

# If root.right exists, then call the invert function and invert the right subtree.

# If both root.left and root.right exist, then swap them

# After all functions returned, we finish inverting the tree. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.left:
            self.invertTree(root.left)

        if root.right:
            self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

# Time complexity: O(n)
# Space complexity: O(h)

# Solution (BFS)

# We use BFS to solve this problem.

# We initiate queue to be a list with root node.
# Then, we pop the last element in the queue out to check its children.

# If node.left exists, we add it to the queue.
# If node.right exists, we add it to the queue.

# Then, we swap node.left and node.right.

# We keep swapping node.left and node.right level by level from up to bottom.
# At the end, we invert the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node.left, node.right = node.right, node.left
        return root

# Time complexity: O(n)
# Space complexity: O(n)