import LinkedList.ListNode;

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode p = head, q = head;

        for (int i = 0; i < n; i++) {
            p = p.next;
        }

        ListNode pre = dummy;
        while (p != null) {
            pre = pre.next;
            p = p.next;
            q = q.next;
        }

        pre.next = q.next;
        q.next = null;

        return dummy.next;
    }
}
