# Input:
# A binary tree

# Output:
# A list of the zigzag level order traversal of nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).

# Solution:
# To solve this problem, we use BFS method.

# We initiate the queue to be the list with root of the tree.
# While queue is not empty, we add the node value to the temp list,
# and add nodes in the next level to the tempq list.
# Then, make tempq to be the queue for the next round of iteration.

# Then, we initiate the flag variable to be 1, and multiplied it by -1 in each iteration.
# When flag is 1, we add temp elements from left to right to the res list.
# When flag is -1, we add temp elements from right to left to the res list.
# In this way, we add nodes of the tree from left to right, then from right to left.

# After all iterations, we print the tree in the zigzag level order in the res list.

# At the end, we return the res list.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        queue = [root]
        flag = 1
        
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
            res.append(temp[::flag])
            flag *= -1
        return res

# Time complexity: O(n)
# Space complexity: O(1)