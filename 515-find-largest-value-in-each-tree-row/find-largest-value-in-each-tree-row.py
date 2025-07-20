# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #we are doing bfs

        q=deque()
        if not root: return []
        q.append(root)
        ans=[]
        while(q):
            curr_max=float('-inf')
            l=len(q)
            for i in range(l):
                node=q.popleft()
                curr_max=max(curr_max,node.val) # tracking current max
                #add left and right child
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(curr_max)
        return ans