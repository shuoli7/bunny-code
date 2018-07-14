# Input:
# A binary tree

# Output:
# A list of the preorder traversal of its nodes' values.
# This means that we want to print out root, left node, right node sequentially.

# Solution 1:
# Iterative (BFS)

# To solve this problem, we can build a result list and a stack for help.
# We store the root into the stack first.
# Then, we pop the top item in the stack out and add it to result list if it is not Null.
# Next, we will store thr right of the node, and the left of the node to the stack.
# While stack is not empty, we will continue to pop items out, and add them to the result list.

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend([node.right, node.left])
        return res
    
# Time complexity: O(n)
# Space complexity: O(1)

# Solution 2:
# Recursive (DFS)

# To solve this problem, we use the recursive method.
# First, we visit the root
# Next, we traverse the left subtree by calling preorderTraversal(left-subtree)
# as well as the right subtree by calling preorderTraversal(right-subtree)
# In the end, we return node, left-subtree, and right-subtree in order.

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
# Time complexity: O(n)
# Space complexity: O(1)