# Input:
# A binary tree

# Output:
# A list of values of tree nodes from preorder traversal
# (traverse nodes in the order of node -> node.left -> node.right).

# Solution 1:
# Iterative (BFS)

# To solve this problem, we can build a stack for help.
# The reason we should use stack is that stack is Last-in-First-out, such that we can do DFS.

# As we traverse down the tree, we push node.right, node.left into the stack.
# and then when we go as far as we can go, we pop the stack out and add its value to res.

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

# To solve this problem, we use the recursion method.

# The base case for the recursion is when root is None, return None.

# Else, we print the node value.

# Then, we traverse the left subtree by calling preorderTraversal(left-subtree)
# as well as the right subtree by calling preorderTraversal(right-subtree).

# After all functions returned, we print node, left-subtree, and right-subtree in order.

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