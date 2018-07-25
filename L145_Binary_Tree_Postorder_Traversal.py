# Input:
# A binary tree

# Output:
# A list of values of tree nodes from preorder traversal
# (traverse nodes in the post order of node.left -> node.right -> node).

# Solution 1:
# Iterative (BFS)

# To solve the problen, we can find a list of values of tree nodes
# in order of node -> node.right -> node.left.
# Then, the reversed list of nodes is in postorder.

# To solve this problem, we can build a stack for help.
# The reason we should use stack is that stack is Last-in-First-out, such that we can do DFS.

# As we traverse down the tree, we push node.right, node.left into the stack.
# and then when we go as far as we can go, we pop the stack out and add its value to res.

# At the end, the reversed res list is what we want

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

# To solve this problem, we use the recursion method.

# The base case for the recursion is when root is None, return None.

# Then, we traverse the left subtree by calling preorderTraversal(left-subtree),
# the right subtree by calling preorderTraversal(right-subtree), and print the node value..

# After all functions returned, we print left-subtree, right-subtree, and node in order.

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
# Time complexity: O(n)
# Space complexity: O(1)