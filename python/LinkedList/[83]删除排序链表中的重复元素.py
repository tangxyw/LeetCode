from .LinkedList import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        while head and head.next:  # 遍历链表, 倒数第一个节点无需遍历
            if head.val == head.next.val:  # 当前节点值和下一个节点值相等, 则当前节点的下一个节点指向下一个节点的下一个节点, 相当与删除了重复元素
                head.next = head.next.next
            else:
                head = head.next  # 当前节点值和下一个节点值不等, 指针向后移动一格

        return dummy.next
