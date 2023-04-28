import LinkedList.ListNode;

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return head;
        
        ListNode tail = head;

        int n = 1;

        while (tail.next != null) {
            tail = tail.next;
            n++;
        }
        tail.next = head;

        k = k % n;

        for (int i = 1; i <= n-k-1; i++) {
            head = head.next;
        }

        ListNode new_head = head.next;
        head.next = null;

        return new_head;
    }
}