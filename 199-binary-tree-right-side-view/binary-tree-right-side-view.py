# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        if not root:
            return right_side_view
        
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                # If this is the last node at the current level, add it to the view
                if i == level_length - 1:
                    right_side_view.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_side_view
        