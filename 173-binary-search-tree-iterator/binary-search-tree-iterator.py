# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        """
        Initialize the iterator with the root of the BST.
        """
        self.stack = []
        self._push_left(root)
        # Push all left children of the root onto the stack

    def _push_left(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left  # Move to the left child 

    def next(self) -> int:
        """
        Return the next smallest number in the BST.
        """
        if not self.stack:
            return None
        node = self.stack.pop()  # Pop the top node from the stack
        self._push_left(node.right)  # Push all left children of the right subtree onto the stack
        return node.val  # Return the value of the popped node
        

    def hasNext(self) -> bool:
        """
        Return whether there is a next smallest number in the BST.
        """
        return len(self.stack) > 0  # Check if the stack is not empty to determine if there are more elements to iterate over
        # isse hum dono halves ko merge karte hain (this merges both halves)
        # Linked list ab reorder ho chuka hai (the linked list is now reordered)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()