# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        Intuition:
        A binary tree is a valid binary search tree if for every node:
        1. All values in the left subtree are less than the node's value.
        2. All values in the right subtree are greater than the node's value.
        3. Both left and right subtrees are valid binary search trees.
        We can use a recursive approach to check these conditions by maintaining a range for each node's value.
        Approach:
        1. Define a helper function that takes a node and the valid range for its value.
        2. If the node is None, return True (an empty tree is a valid BST).
        3. Check if the node's value is within the valid range.
        4. Recursively check the left and right subtrees with the updated valid range.
        5. Return True if both subtrees are valid, otherwise return False.
        '''
        def helper(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (helper(node.left, low, node.val) and helper(node.right, node.val, high))
        return helper(root)
        