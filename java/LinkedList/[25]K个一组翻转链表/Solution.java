import LinkedList.ListNode;

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null) return head;

        ListNode tail = head;
        for (int i = 1; i < k; i++) {
            if (tail == null || tail.next == null) return head;
            tail = tail.next;
        }

        ListNode new_head = reverseKGroup(tail.next, k);

        ListNode cur = head;
        ListNode post = cur.next;
        for (int j = 1; j < k; j++) {
            ListNode tmp = post.next;
            post.next = cur;
            cur = post;
            post = tmp; 
        }

        head.next = new_head;

        return tail;

    }
}