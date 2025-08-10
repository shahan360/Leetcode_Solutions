"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def helper(root, result):
            if root == None:
                return
            for i in range(0,len(root.children)):
                helper(root.children[i], result)
            result.append(root.val)
        
        result = []
        helper(root, result)
        return result
        
        