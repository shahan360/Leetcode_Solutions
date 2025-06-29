# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        slow = fast = head # humne slow aur fast pointers ko head se initialise kiya hai. (We have initialized both slow and fast pointers to the head of the linked list.)
        # Traverse the linked list with slow moving one step and fast moving two steps
        while fast is not None and fast.next is not None: # jab tak fast pointer None nahi hai aur fast ka next pointer bhi None nahi hai, tab tak loop chalega. (This loop will run until the fast pointer is not None and the fast's next pointer is also not None.)
            slow = slow.next # slow pointer ko ek step aage badhaenge. (We will move the slow pointer one step forward.)
            fast = fast.next.next # fast pointer ko do steps aage badhaenge. (We will move the fast pointer two steps forward.)
        # When fast pointer reaches the end, slow pointer will be at the middle element
        # jab fast pointer end tak pahunchta hai, toh slow pointer middle element par hoga. (When the fast pointer reaches the end, the slow pointer will be at the middle element
        return slow # middle element return karega. (This will return the middle element.)