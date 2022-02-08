# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Sort the node values first
        node_list = []
        p,q,i = head, head, 0
        while p:
            node_list.append(p.val)
            p = p.next
        
        node_list.sort()
        
        # Assign sorted values to the linked list
        while q:
            q.val = node_list[i]
            i += 1
            q = q.next
        
        return head
        
#         # This solution cannot handlle overall sort.
#         # [4,2,1,3] => [2,1,3,4]  / while correct answer should be [1,2,3,4]
#         p, q = head, head.next
#         while not p is None and not q is None:
            
#             if p.val > q.val:  # inter-change node values
#                 tmp = p.val
#                 p.val = q.val
#                 q.val = tmp
#             else:
#                 p = p.next  
#                 q = q.next     # move forward
        
#         return head