from .LinkedList import ListNode
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # 先计算链表长度n
        cur = head
        n = 1
        while cur and cur.next:
            cur = cur.next
            n += 1

        # 此时cur为链表尾部, cur.next指向head, 使得链表成环
        cur.next = head

        # 化简k, 使得k在[0, n-1]中
        k = k % n

        # head向前移动rotate步后断开环, rotate在[0, n-1]中
        rotate = n - k - 1
        while rotate > 0:
            head = head.next
            rotate -= 1

        new_head = head.next
        head.next = None

        return new_head
