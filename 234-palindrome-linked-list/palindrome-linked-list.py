# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev = None
        curr = slow

        while curr:
            save = curr.next
            curr.next = prev
            prev = curr
            curr = save

        curr1 = head
        curr2 = prev

        while curr2:
            if curr1.val == curr2.val:
                curr1 = curr1.next
                curr2 = curr2.next
            else:
                return False

        return True
        