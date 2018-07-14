# Input:
# A binary tree

# Output:
# A list of the inorder traversal of its nodes' values.
# This means that we want to print out left node, right node, and root sequentially.

# Solution 1:
# Iterative (BFS)

# To solve this problem, we can achieve a Root-Right-Left traverse (similar as preorder traverse)
# and return the reversed result (Left-Right-Root)

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend([node.left, node.right])
        return res[::-1]
    
# Time complexity: O(n)
# Space complexity: O(1)

# Solution 2:
# Recursive (DFS)

# To solve this problem, we use the recursive method.
# First, we build a helper.
# Then, we traverse the left subtree by calling helper(left-subtree)
# Next, we add root value to the result.
# Then, we traverse the right subtree by calling helper(right-subtree)

# In the end, we return left-subtree, node, and right-subtree in order.
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if not root:
            return []
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)
        
# Time complexity: O(n)
# Space complexity: O(1)