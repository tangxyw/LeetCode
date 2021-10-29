from .CreateTree import TreeNode
from typing import List


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # BFS, 层次遍历
        if not root:
            return []
        q = [root]
        res = []

        while q:
            tmp = []
            # 取每层第一个节点值
            res.append(q[0].val)
            for node in q:  # 先右后左
                if node.right:
                    tmp.append(node.right)
                if node.left:
                    tmp.append(node.left)
            q = tmp

        return res
