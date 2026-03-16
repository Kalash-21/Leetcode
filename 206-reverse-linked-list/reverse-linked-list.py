# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # While loop
        # curr=head
        # prev=None
        # while curr:
        #     save=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=save
        # return prev

        # Recurison

        def rev(curr,prev):
            if curr==None:
                return prev
            else:
                save=curr.next
                curr.next=prev
                return rev(save,curr)
        return rev(head, None)


        
        