# Input:
# A binary tree

# Output:
# A list of values of tree nodes from inorder traversal
# (traverse nodes in the order of node.left -> node -> node.right).

# Solution 1:
# Iterative (DFS)

# To solve this problem, we can build a stack for help.
# The reason we should use stack is because we need to go over all leftmost nodes before printing
# in order to achieve inorder traversal.

# If the root is not None, we add the root into the stack.
# Then we make root.left to be the new root and keep checking if it is None or not.

# If the root.left is None, it means the top node in the stack is the leftmost node.
# So, we pop it out and add its value to result list.

# Next, we will make the node.right to the new root, and continue the iteration.

# When root is None and stack is empty, it means that all nodes in the tree have been added
# to the result list. So we should stop and return result list.

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while root or stack:
            if root: # DFS goes to the left-most leaf
                stack.append(root)
                root = root.left
            else: # node.left is None, print out node value, then check its right node
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res
    
# Time complexity: O(n)
# Space complexity: O(h) # h is the height of the binary tree

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
# Space complexity: O(h) # h is the height of the binary tree