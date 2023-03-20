from .LinkedList import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
