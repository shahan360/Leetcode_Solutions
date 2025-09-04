# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next is not None and current.next.next is not None:
            first = current.next
            second = current.next.next

            #Swapping pointers
            first.next  = second.next
            second.next = first
            current.next = second

            # Move current pointer two nodes forward for next Swapping
            current = first
        
        head = dummy.next

        return head


        