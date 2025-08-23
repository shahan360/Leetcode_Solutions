# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: # Agar root khaali hai (if root is empty)
            return [] # toh khaali list wapas karo (return an empty list)

        result = [] # yeh result list hai (this is the result list)
        queue = [root] # humne root ko queue mein daala (we added the root to the queue)
        while queue: # jab tak queue khaali nahi hoti (while the queue is not empty)
            level_size = len(queue) # yeh current level ke nodes ki sankhya hai (this is the number of nodes at the current level)
            current_level = [] # yeh current level ki list hai jahaan hum node values daalenge (this is the list for the current level where we will add node values)
            for _ in range(level_size): # yeh loop current level ke nodes par chalega (this loop will run for each node at the current level)
                node = queue.pop(0) # yeh node ko queue se nikaal raha hai (this removes the node from the queue)
                current_level.append(node.val) # yeh node ki value ko current level mein daal raha hai (this adds the node's value to the current level)
                if node.left is not None: # agar node ka left child hai (if the node has a left child)
                    queue.append(node.left) # toh usse queue mein daal do (add it to the queue)
                if node.right is not None: # agar node ka right child hai (if the node has a right child)
                    queue.append(node.right) # toh usse queue mein daal do (add it to the queue)
            result.append(current_level) # current level ki list ko result mein daal do (add the current level list to the result)
        return result # result ko wapas karo (return the result)

# Dry Run
# Let's do a dry run of the algorithm with the following binary tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
# The expected output is [[1], [2, 3], [4, 5, 6]]

# Dry Run Visualization
# Let's visualize the dry run step by step:

# Initial Queue: [1]
# Level 0:
#   Dequeue: 1
#   Enqueue: 2, 3
#   Current Level: [1]
# Result: [[1]]

# Level 1:
#   Dequeue: 2
#   Enqueue: 4, 5
#   Dequeue: 3
#   Enqueue: 6
#   Current Level: [2, 3]
# Result: [[1], [2, 3]]

# Level 2:
#   Dequeue: 4
#   Dequeue: 5
#   Dequeue: 6
#   Current Level: [4, 5, 6]
# Result: [[1], [2, 3], [4, 5, 6]]

# Visualization Tree by each Level:
# Level 0:      1
#              / \
# Level 1:    2   3
#            / \   \
# Level 2:  4   5   6
 