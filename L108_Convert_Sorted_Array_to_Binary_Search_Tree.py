# Input
# A sorted array, where elements are in ascending order.

# Output
# A height balanced binary search tree

# (The benefit of BST is the time complexity of searching and inserting is O(logn))

# Solution:
# As we want to get a height balanced BST,
# we can pick the mid number in the list to be the root,
# numbers in the left is the left subtree;
# numbers in the right is the right subtree.
# So we recursively call the function itself to generate the BST.

# The base case has two cases.

# If the list did not exist, return None.
# If there is only one element, that is the only treenode.

# Else, the mid number in the list is the root.
# We recursively call the function itself to get left-subtree
# based on numbers from beginning to the mid;
# And we recursively call the function itself to get right-subtree
# based on numbers from mid to the end;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
        	return None
        if length == 1:
        	return TreeNode(nums[0])
        mid = int(length / 2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

# Time complexity: O(n)
# Space complexity: O(h) # h is the height of the tree
