/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode temp = new ListNode(0);
        ListNode output = temp;
        int sum = 0;
        
        while (l1 != null || l2 != null || sum > 0) {        // need "or" operation for the case which has diff length of numbers, and sum > 0 is for the case that has only carry
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            //sum += l1.val + l2.val;    // change this line into previous blocks
            temp.next = new ListNode(sum % 10);    // the remainder
            sum /= 10;             // quotient
            
            temp = temp.next;      // go to the next node
        }
        
        return output.next;
    }
}