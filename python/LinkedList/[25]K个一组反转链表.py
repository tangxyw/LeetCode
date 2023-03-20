from typing import Optional
from .LinkedList import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 后序遍历
        if not head:
            return head

        # 向后探索
        tail = head
        for _ in range(k - 1):
            if not tail or not tail.next:
                # 不足k个节点, 直接返回
                return head
            tail = tail.next

        # 这时tail为本次递归head后面第k个节点

        # 向后递归
        new_head = self.reverseKGroup(tail.next, k)

        # 反转操作
        cur = head
        post = cur.next
        for _ in range(k - 1):
            tmp = post.next
            post.next = cur
            cur = post
            post = tmp

        # head后面接下层递归结果
        head.next = new_head

        # tail变成了头结点
        return tail
