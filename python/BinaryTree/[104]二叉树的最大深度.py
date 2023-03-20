from typing import List
from CreateTree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 广度优先搜索BFS
        q = []
        if root:
            q.append(root)
        else:
            return 0

        depth = 0
        while len(q) > 0:
            tmp = []
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
            depth += 1

        return depth
