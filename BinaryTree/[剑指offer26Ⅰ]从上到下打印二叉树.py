from typing import List
from CreateTree import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # 层次遍历
        if not root:
            return []
        q = [root]
        res = []
        while q:
            tmp = []
            for node in q:
                res.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp

        return res