# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next # pointer to next
            curr.next = prev # redirecting next pointer to the previous pointer
            prev = curr # setting previous pointer to current pointer - will become in next iteration next
            curr = temp # progressing pointers
        return prev





    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head 

        while curr:
            temp = curr.next # pointer to next 
            curr.next = prev # next points now to prev
            prev = curr # prev is now curr
            curr = temp # current proceeds
        return prev

            

