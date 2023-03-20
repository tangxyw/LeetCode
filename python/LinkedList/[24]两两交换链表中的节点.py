from .LinkedList import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        tmp = dummy
        while tmp.next and tmp.next.next:   # tmp为待交换的两个node之前的节点
            node1 = tmp.next
            node2 = tmp.next.next
            # 交换两个节点位置
            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            tmp = node1 # 更新tmp，进入下一轮迭代