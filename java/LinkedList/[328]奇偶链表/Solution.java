import LinkedList.ListNode;

class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode p = head;
        ListNode q = head.next;
        ListNode anchor = q;

        while (q != null && q.next != null) {
            p.next = q.next;
            p = q.next;
            q.next = p.next;
            q = p.next;
        }

        p.next = anchor;

        return head;
    }
}