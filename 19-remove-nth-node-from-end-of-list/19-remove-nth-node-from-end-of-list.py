# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Don't have to directly use head. Need to copy as pointers and use them!
        fakehead = ListNode(0, head) # put 0 in front of head
        p = fakehead  # slow
        q = fakehead  # fast
        
        count = 0
        while q.next:
            if count >= n:
                p = p.next
                q = q.next
            else:
                q = q.next
            count += 1
        
        p.next = p.next.next
        
        return fakehead.next