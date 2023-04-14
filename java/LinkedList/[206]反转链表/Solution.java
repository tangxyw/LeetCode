import LinkedList.ListNode;

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode new_head = reverseList(head.next);
        
        head.next.next = head;
        head.next = null;

        return new_head;

    }
}