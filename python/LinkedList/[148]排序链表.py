from .LinkedList import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 归并排序, 递归
        if not head or not head.next:
            return head

        # 将链表一分为二, 分别排序
        middle = self.findMiddleNode(head)  # 找到中间结点
        l2_head = middle.next  # 第二个链表的head
        middle.next = None  # 切断

        # 向下递归
        l1 = self.sortList(head)
        l2 = self.sortList(l2_head)

        return self.mergeTwoLists(l1, l2)

    def findMiddleNode(self, head: ListNode) -> ListNode:
        """找到链表的中间结点, 奇数个节点返回正中间节点, 偶数个节点返回中间靠左节点(不能返回靠右节点, 否则会无限递归)"""
        if not head or not head.next:  # 链表为空或只有1个节点
            return head

        dummy = ListNode(0)
        dummy.next = head

        # 双指针
        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """合并两个有序链表, 参考[21]题"""
        # 递归
        # 参数: l1, l2
        # 终止条件: l1 or l2 is None
        # 本次递归任务: 找到备选节点, 并指定备选节点的next
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:  # l1的节点值更小
            l1.next = self.mergeTwoLists(l1.next, l2)  # 将l1拿出, 指定l1的下一个节点为下层递归返回值
            return l1  # 要l1本身返回给上层递归
        else:  # l2的节点值更小, 同上
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



