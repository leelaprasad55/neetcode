# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        p=None
        while t:
            n=t.next
            t.next=p
            p=t
            t=n
        return p
        