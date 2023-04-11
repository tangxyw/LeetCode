import LinkedList.ListNode;

class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode middle = findMiddleNode(head);
        ListNode l2_head = middle.next;
        middle.next = null;

        ListNode l1 = sortList(head);
        ListNode l2 = sortList(l2_head);

        return mergTwoLists(l1, l2);
    }

    private ListNode mergTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        if (l1.val < l2.val) {
            l1.next = mergTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergTwoLists(l1, l2.next);
            return l2;
        }
    }

    private ListNode findMiddleNode(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode slow = dummy, fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        return slow;
    }
}