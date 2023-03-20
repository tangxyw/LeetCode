from .LinkedList import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 锚节点, 删除节点的时候通常要构造
        dummy = ListNode(0)
        dummy.next = head
        # 双指针
        p, q = head, head
        # p 先往前走n步
        for i in range(n):
            p = p.next
        # p和q一起走, 直到p指向末尾null, 这时q正好指向待删除节点
        pre = dummy
        while p:
            pre = pre.next  # pre永远是q前面的那个节点
            p = p.next
            q = q.next

        pre.next = q.next  # q前面节点pre的下一个节点指向q的下一个节点, 这样就删除了q
        q.next = None  # q与下一个节点也断开
        return dummy.next  # 若pre是dummy, 说明p是head, 这时删除了head; 若pre不是dumpy, 说明没有删除head, 而dummy.next也就是head
