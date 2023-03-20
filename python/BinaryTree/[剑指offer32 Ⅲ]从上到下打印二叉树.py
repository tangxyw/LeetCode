from typing import List
from CreateTree import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        depth = 1   # 树深度

        while q:
            tmp = []
            layer_res = []  # 每层节点值
            for node in q:
                layer_res.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            # 深度为奇数时正向打印, 为偶数时反向打印
            if depth % 2 == 1:
                res.append(layer_res)
            else:
                res.append(layer_res[::-1])
            q = tmp
            depth += 1

        return res