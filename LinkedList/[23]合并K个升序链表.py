from .LinkedList import ListNode
from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        cadidates = []  # 候选节点集合
        for node in lists:
            if node:
                cadidates.append(node)

        dummy = ListNode(-1)  # 锚节点
        p = dummy  # 当前结点指针
        while cadidates:  # 迭代直到候选节点集合为空
            min_val = float('inf')  # 每轮迭代前都恢复最小值定义
            for node in cadidates:  # 选出最小值
                if node.val < min_val:
                    min_val = node.val
                    cur = node  # 最小值对应的头节点
            p.next = cur  # 当前指针next指向cur
            p = cur  # 更新当前指针到cur
            cadidates.remove(cur)  # 移除cur
            if cur.next:  # 添加新候选
                cadidates.append(cur.next)

        return dummy.next
