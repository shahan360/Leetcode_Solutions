# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, 0)
        return self.sum

    def dfs(self, node: Optional[TreeNode], current_sum: int):
        if not node:
            return
        current_sum = current_sum * 10 + node.val
        if not node.left and not node.right:
            self.sum += current_sum
        self.dfs(node.left, current_sum)
        self.dfs(node.right, current_sum)