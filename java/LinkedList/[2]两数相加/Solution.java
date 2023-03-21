import LinkedList.ListNode;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return helper(l1, l2, 0);
        }
    
    public ListNode helper(ListNode l1, ListNode l2, int add_one) {
        if (l1 == null && l2 == null && add_one == 0) {
            return null;
        }
        // 两个加数
        int p1 = l1 != null ? l1.val : 0;
        int p2 = l2 != null ? l2.val : 0;

        // 本位上的数字 
        int sum = (p1 + p2 + add_one) % 10;

        // 是否进位
        add_one = (p1 + p2 + add_one) / 10;

        ListNode cur = new ListNode(sum);
        // 向后递归
        l1 = l1 != null ? l1.next : null;
        l2 = l2 != null ? l2.next : null;
        cur.next = helper(l1, l2, add_one);

        return cur;
    }
}