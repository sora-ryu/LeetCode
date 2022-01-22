# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged = []
        
        # Get List1 elements
        while list1:
            merged.append(list1.val)
            list1 = list1.next
            
        # Get List2 elements
        while list2:
            merged.append(list2.val)
            list2 = list2.next
        
        # Sort the merged list
        merged.sort()
        
        # Return the head of the merged linked list
        answer = ListNode(0)
        tmp = answer
        
        for i in range(len(merged)):
            tmp.next = ListNode(merged[i])
            tmp = tmp.next
        
        return answer.next
        