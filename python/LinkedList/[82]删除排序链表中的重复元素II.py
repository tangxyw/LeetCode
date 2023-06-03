from .LinkedList import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head

        while cur:
            # cur.next存在, 且和下一个节点的val相同
            while cur.next and cur.val == cur.next.val:
                cur = cur.next  # cur移动到重复值的最后一个位置
            if pre.next == cur:  # 巧妙判断是否前面有重复值
                pre = pre.next  # 如果没有, pre后移
            else:
                pre.next = cur.next  # 如果有, pre指向最后一个重复值的后面
            cur = cur.next  # cur后移

        return dummy.next
