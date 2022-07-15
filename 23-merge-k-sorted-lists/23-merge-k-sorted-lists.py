# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        merged_values, ans = [], ListNode(0)
        for list1 in lists:
            while list1:
                merged_values.append(list1.val)
                list1 = list1.next
        
        p = ans  #copy the head
        for v in sorted(merged_values):
            p.next = ListNode(v)
            p = p.next
        
        
        return ans.next
        