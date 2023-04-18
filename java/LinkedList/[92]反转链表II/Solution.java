import LinkedList.ListNode;

class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode pre = dummy;

        for (int i = 0; i < left - 1; i++) {
            head = head.next;
            pre = pre.next;
        }

        ListNode right_node = head;
        for (int j = 0; j < right - left; j++) {
            right_node = right_node.next;
        }
        ListNode post = right_node.next;

        reverseBetween(head, right_node);

        pre.next = right_node;
        head.next = post;

        return dummy.next;

    }

    private void reverseBetween(ListNode head, ListNode right_node) {
        if (head == right_node) return;

        reverseBetween(head.next, right_node);

        head.next.next = head;
        head.next = null;

        return;

    }
}