from .CreateTree import TreeNode
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []  # 最终结果
        q = [root]
        while q:
            tmp = []
            res_layer = []  # 存放每一层的节点值
            for node in q:  # 遍历本层节点
                res_layer.append(node.val)  # 节点值依次放入res_layer
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(res_layer)
            q = tmp

        return res
