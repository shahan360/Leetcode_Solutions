# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Brute force approach: Convert linked list to a list and check if it is a palindrome. Here, Time Complexity is O(n) and Space Complexity is O(n) because we are using an additional list to store the values of the linked list.
        nums = [] # humne ek empty list banayi hai jisme linked list ke values store karenge (We created an empty list to store the values of the linked list)
        while head is not None: # jab tak head None nahi hai tab tak hum values ko list me append karte rahenge (We will keep appending values to the list until the head is None)
            nums.append(head.val) # hum head ke value ko list me append karte hain (We append the value of the head to the list)
            head = head.next # head ko next node par le jaate hain (We move the head to the next node)
        # ab hum check karte hain ki kya list palindrome hai (Now we check if the list is a palindrome)
        # hum left aur right pointers banate hain (We create left and right pointers)
        
        left, right = 0, len(nums) - 1 # left pointer ko 0 par aur right pointer ko last index par set karte hain (We set the left pointer to 0 and the right pointer to the last index)
        while left < right: # jab tak left pointer right pointer se chhota hai tab tak hum check karte hain (We check until the left pointer is less than the right pointer)
            if nums[left] != nums[right]: # agar left aur right pointers ke values alag hain toh yeh palindrome nahi hai (If the values at the left and right pointers are not equal, then it is not a palindrome)
                return False # hum False return karte hain (We return False)
            else: # agar values barabar hain toh hum left aur right pointers ko update karte hain (If the values are equal, we update the left and right pointers)
                left += 1 # hum left pointer ko aage badhate hain (We move the left pointer forward)
                right -= 1 # hum right pointer ko peeche le jaate hain (We move the right pointer backward)
        return True # agar humne loop complete kar liya toh yeh palindrome hai (If we complete the loop, then it is a palindrome)