# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node before position left (left-1 steps)
        for _ in range(left - 1):
            prev = prev.next
        
        # set start to left, this will be first node of reversed sublist
        start = prev.next
        then = start.next

        # Reverse sublist from left to right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next
        