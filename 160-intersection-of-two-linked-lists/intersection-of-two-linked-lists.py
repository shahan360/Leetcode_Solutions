# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        Intuition:
        Two pointers currA and currB traverse the two linked lists. they keep track of the lengths of the lists.
        When one pointer reaches the end, it starts traversing the other list.If there is an intersection, the two pointers will meet at the intersection node.
        If there is no intersection, both pointers will reach the end of their respective lists at the same time.
        Time Complexity: O(m + n), where m and n are the lengths of the two linked lists.
        Space Complexity: O(1), as we are using only two pointers.
        '''
        if not headA or not headB:
            return None
        currA, currB = headA, headB
        lenA, lenB = 0, 0
        while currA is not None:
            lenA += 1
            currA = currA.next
        while currB is not None:
            lenB += 1
            currB = currB.next
        currA, currB = headA, headB
        while lenA > lenB:
            currA = currA.next
            lenA -= 1
        while lenB > lenA:
            currB = currB.next
            lenB -= 1
        while currA is not None and currB is not None:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None