from .LinkedList import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 迭代
        dummy = ListNode(-1)
        dummy.next = head
        tmp = dummy
        while tmp.next and tmp.next.next:  # tmp为待交换的两个node之前的节点
            node1 = tmp.next
            node2 = tmp.next.next
            # 交换两个节点位置
            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            tmp = node1  # 更新tmp，进入下一轮迭代

    def swapPairs2(self, head: ListNode) -> ListNode:
        # 递归, 先序
        if not head or not head.next:   # 最后一个单独node或者None
            return head

        # 记录head后面2个node
        three = head.next.next
        next = head.next

        # 反转head和next
        next.next = head
        # head的next由下层递归给出
        head.next = self.swapPairs(three)

        # 新头结点变成了原head的下一个node, 作为递归返回值
        return next
