from .LinkedList import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_p = ListNode(None)  # 节点值小于x的哨兵节点
        dummy_q = ListNode(None)  # 节点值大于等于x的哨兵节点
        p, q = dummy_p, dummy_q  # p,q分别为小于x和大于等于x的链表指针
        cur = head

        while cur:  # 遍历原链表
            if cur.val < x:  # 节点值<x, 则将节点链接到p后面, 再讲p指向当前节点
                p.next = cur
                p = p.next
            else:  # 节点值>=x, 逻辑同上
                q.next = cur
                q = q.next
            cur = cur.next  # cur后移

        q.next = None  # 切断q的尾部
        p.next = dummy_q.next  # 将q链接到p的后面

        # 返回p(此逻辑包含了head为空 or p为空 or q为空)
        return dummy_p.next
