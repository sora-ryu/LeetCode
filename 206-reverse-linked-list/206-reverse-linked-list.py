# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        
        reversed_list1 = list1[::-1]
        head = ListNode(0)  # Initialize
        p = head
        for i in reversed_list1:
            p.next = ListNode(i)
            p = p.next  # move pointer to the next node
        
        return head.next