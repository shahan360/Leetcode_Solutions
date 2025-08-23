# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: # Agar root None hai toh khali list return karo (if root is None then return Empty list)
            return [] # toh khaali list wapas karo (return an empty list)

        result = [] # Yeh result list hai jisme hum final output store karenge (This is the result list where we will store the final output)

        queue = [root] # Yeh queue hai jisme hum nodes ko store karenge (This is the queue where we will store the nodes)
        left_to_right = True # Yeh indicate karta hai ki hum left se right ya right se left traverse kar rahe hain
        while queue: # Jab tak queue khali nahi hoti (While the queue is not empty)
            level_size = len(queue) # Yeh queue ke current level ki size hai (This is the size of the current level)
            current_level = [] # Yeh current level ki values store karne ke liye hai (This is to store the values of the current level)
            for _ in range(level_size): # Yeh loop current level ke nodes ko process karne ke liye hai (This loop is to process the nodes of the current level)
                node = queue.pop(0) # Yeh node ko queue se nikaal raha hai (This is to remove the node from the queue)
                current_level.append(node.val) # Yeh current level mein node ka value add kar raha hai (This is to add the node's value to the current level)
                if node.left is not None: # Agar left child hai toh queue mein daal do (If left child exists, add it to the queue)
                    queue.append(node.left) # Yeh left child ko queue mein daal raha hai (This is to add the left child to the queue)
                if node.right is not None: # Agar right child hai toh queue mein daal do (If right child exists, add it to the queue)
                    queue.append(node.right) # Yeh right child ko queue mein daal raha hai (This is to add the right child to the queue)

            if not left_to_right: # Agar left se right nahi ja rahe hain (If we are not going left to right)
                current_level.reverse() # Toh current level ko reverse kar do (Then reverse the current level)
            result.append(current_level) # Yeh current level ko result mein daal raha hai (This is to add the current level to the result)
            left_to_right = not left_to_right # Yeh left_to_right ko toggle kar raha hai (This is to toggle the left_to_right flag)
        return result # Yeh final result ko wapas kar raha hai (This is to return the final result)


# Dry Run
# Let's do a dry run of the algorithm with the following binary tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
# The expected output is [[1], [3, 2], [4, 5, 6]]

# Dry Run using the above binary tree:
# Level 0:
#   Queue: [1]
#   Current Level: [1]
#   Result: [[1]]
#
# Level 1:
#   Queue: [2, 3]
#   Current Level: [3, 2]
#   Result: [[1], [3, 2]]
#
# Level 2:
#   Queue: [4, 5, 6]
#   Current Level: [4, 5, 6]
#   Result: [[1], [3, 2], [4, 5, 6]]