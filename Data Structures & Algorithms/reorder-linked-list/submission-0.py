# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        if not h or not h.next:
            return
        s=h
        f=h
        while f.next and f.next.next:
            s=s.next
            f=f.next.next
        p=None
        c=s.next
        while c:
            n=c.next
            c.next=p
            p=c
            c=n
        s.next=None
        c1=h
        c2=p
        while c2:
            n1=c1.next
            n2=c2.next
            c1.next=c2
            c2.next=n1
            c1=n1
            c2=n2
        


