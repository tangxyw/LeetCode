from typing import Optional
from CreateTree import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        if not root:
            return res

        q = [(root, 1)]

        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)  # 计算当前层最大宽度并比较
            tmp = []
            for node, index in q:   # 按层给每个node从左到右编号
                if node.left:
                    tmp.append((node.left, index * 2))
                if node.right:
                    tmp.append((node.right, index * 2 + 1))
            q = tmp

        return res
