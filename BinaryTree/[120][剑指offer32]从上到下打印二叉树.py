from typing import List
from CreateTree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 层次遍历, 深度优先
        if not root:
            return []
        q = []
        q.append(root)
        res = []
        while q:
            layer_nodes = []  # 存放每层节点的值
            tmp = []
            for node in q:
                layer_nodes.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(layer_nodes)
            q = tmp

        return res