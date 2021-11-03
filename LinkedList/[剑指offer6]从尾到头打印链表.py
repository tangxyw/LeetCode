from .LinkedList import ListNode
from typing import List


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 前序遍历
        self.res = []

        def preorder(head: ListNode):
            if not head:  # base case, 到了末尾
                return
            # 递归下一个节点
            preorder(head.next)
            self.res.append(head.val)

        preorder(head)
        return self.res
