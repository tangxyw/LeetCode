from .CreateTree import TreeNode
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        res = []
        depth = 0  # 当前遍历深度, 根节点为0

        while q:
            tmp = []
            n = len(q)
            for i in range(n):
                cur = q.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if depth % 2 == 0:
                res.append(tmp)
            if depth % 2 == 1:  # 奇数层倒序
                res.append(tmp[::-1])
            depth += 1  # 深度自增1

        return res
