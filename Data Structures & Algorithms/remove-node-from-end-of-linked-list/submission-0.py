# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        t=head
        while t:
            c+=1
            t=t.next
        c=c-n
        if c==0:
            return head.next
        t=head
        p=None
        c1=0
        while t:
            if c==c1:
                p.next=t.next
                break
            else:
                c1+=1
                p=t
                t=t.next
        return head