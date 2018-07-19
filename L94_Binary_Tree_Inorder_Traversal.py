# Input:
# A binary tree

# Output:
# A list of values of tree nodes from inorder traversal
# (traverse nodes in the order of node.left -> node -> node.right).

# Solution 1:
# Iterative (DFS)

# To solve this problem, we can build a stack for help.
# The reason we should use stack is that stack is Last-in-First-out, such that we can do DFS.
# As we traverse down to the left, we push nodes into the stack.
# and then when we go as far left as we can go , we pop the node out and print its value.

# Basically, we go left first. Print everything that is down left. Then we go up, and print.
# Then we go down to right and see if we can go left again.

# If the root is not None, we add the root into the stack.
# Then we make root.left to be the new root and keep checking if it is None or not.

# If the root.left is None, it means the top node in the stack is the candidate node
# that is ready to be printed.
# So, we pop it out and print its value.
 
# Next, we will make the node.right to the new root, and continue the iteration with the same logic.

# When root is None and stack is empty, it means that all nodes in the tree have been visited 
# ans their values have been added to the result list. So we should stop and return result list.

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

# We define a helper function, which takes root node and result list as arguments.
# We call this helper function inside inorderTraversal().

# In the helper function, we first define the return condition to be root equals to None.

# As we need to go all the way down to the left first,
# we recursively call helper function to the root.left
# until we reach the left-most node whose left child is None,
# then we know that this is the candidate node to be printed out.

# After we print out the root node, we move to the right.
# Then we recursively call helper function again,
# this time we take root.right as root and repeat the same logic.

# After all functions returned, we go back to the top level call in inorderTraversal function,
# we will have all node values in the result list, so we can return the result list.

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