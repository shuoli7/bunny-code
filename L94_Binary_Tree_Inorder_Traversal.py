# Input:
# A binary tree

# Output:
# A list of the inorder traversal of its nodes' values.
# This means that we want to print out left node, root, right node sequentially.

# Solution 1:
# Iterative (BFS)

# To solve this problem, we can build a result list and a stack for help.
# If the root is not empty, we store the root into the stack, and make root.left to be the new root.
# We keep doing that until there is not root.left.
# At this time, we add all nodes in the leftmost branch to the stack.

# Then, if the stack is not empty, we pop the top item in the stack out and add it to result list.
# In this way, we add the node.left in the result list.

# Next, we will add the node, and the node.right to the result.

# When stack is empty, we stop. At this time, we have added all nodes in the tree to the result list.

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                res.append(node.val)
                root = node.right
            else:
                return
    
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
    def inorderTraversal(self, root):
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
        res.append(root.val)
        self.helper(root.right, res)
    
# Time complexity: O(n)
# Space complexity: O(1)