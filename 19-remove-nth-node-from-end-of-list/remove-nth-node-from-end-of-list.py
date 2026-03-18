# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=dummy
        fast=dummy
        check=0
        while n+1!=check:
            check+=1
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next


        slow.next=slow.next.next
        return dummy.next