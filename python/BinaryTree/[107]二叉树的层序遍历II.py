from .CreateTree import TreeNode
from typing import List


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]
        while q:
            n = len(q)
            tmp = []
            for i in range(n):  # 遍历次数为q的长度, 即迭代完本层所有节点
                cur = q.pop(0)  # 每次取q[0], 且pop出q[0]
                tmp.append(cur.val)  # 记录当前val
                # 再把下一层的节点放在q的后面
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(tmp)

        # 倒转res返回
        return res[::-1]
