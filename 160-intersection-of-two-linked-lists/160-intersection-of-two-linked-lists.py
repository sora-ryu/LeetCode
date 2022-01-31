# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None
        
        # headA = A + O, headB = B + O  (O : the repeated part)
        # Eventually, it goes the same length (A+O+B = B+O+A)
        p, q = headA, headB  # Use two pointers
        
        while p != q:
            if p is not None:
                p = p.next
            else:
                p = headB
            if q is not None:
                q = q.next 
            else:
                q = headA
            
        return p