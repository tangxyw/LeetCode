import LinkedList.ListNode;

class Solution {
    private ListNode left_head;

    public boolean isPalindrome(ListNode head) {
        this.left_head = head;

        return postorder(head);
    }

    private boolean postorder(ListNode head) {
        if (head == null) return true;

        boolean curr_res = postorder(head.next);

        if (curr_res == false) return false;

        if (head.val != left_head.val) return false;

        left_head = left_head.next;

        return true;
    }
}