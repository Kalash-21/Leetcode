
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        if not head:
            return False
        fast , slow = curr, curr 

        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True 
        return False   