# Input:
# A binary tree

# Output:
# A list of the bottom-up level order traversal of nodes' values.
# (ie, from left to right, level by level from leaf to root).

# Solution:
# To solve this problem, we use BFS method.
# We print the tree from root to leaf level by level, from left to right in the res list.
# At the end, we should return the reversed list.

# We initiate the queue to be the list with root of the tree.
# While queue is not empty, we add the node value to the temp list,
# and add nodes in the next level to the tempq list.
# Then, make tempq to be the queue, and add temp the res list.
# After all iterations, we print the tree from up to bottom in the res list.

# At the end, we return the reversed res list.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res, queue = [], [root]
        while queue:
            temp = []
            tempq = []
            for node in queue:
                temp.append(node.val)
                if node.left:
                    tempq.append(node.left)
                if node.right:
                    tempq.append(node.right)
            queue = tempq
            res.append(temp)
        return res[::-1]

# Time complexity: O(n)
# Space complexity: O(1)