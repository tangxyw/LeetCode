from CreateTree import TreeNode

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 层次遍历, 广度优先
        if not root:
            return 0
        q = [root]
        depth = 1
        while q:
            tmp = []
            for node in q:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
            depth += 1