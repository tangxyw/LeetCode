import LinkedList.ListNode;

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pa = headA, pb = headB;

        while (pa != pb) {
            pa = pa != null ? pa.next : headB;
            pb = pb != null ? pb.next : headA;
        }
        
        return pa;
    }
}