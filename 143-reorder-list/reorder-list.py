# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reorderList(self, head: Optional['ListNode']) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        Intuition:
        1. Find the middle of the linked list using the slow and fast pointer technique.
        2. Reverse the second half of the linked list.
        3. Merge the two halves of the linked list.
        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(1), as we are modifying the linked list in-place.
        '''
        if not head or not head.next:
            return 
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # Step 2: Reverse the second half of the linked list
        fast = self.reverseList(slow.next)
        # Disconnect the first half from the second half       
        slow.next = None
        slow = head
        # Step 3: Merge the two halves of the linked list
        while fast is not None:
            temp = slow.next
            slow.next = fast
            fast = fast.next
            slow.next.next = temp
            slow = temp
        # The linked list is now reordered in-place

    def reverseList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
