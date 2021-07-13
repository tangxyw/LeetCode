from typing import List
from CreateTree import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root: TreeNode, path: str):
            # 注意这里的path参数不要使用list, 会被当作指针
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:    # 到达叶子节点
                res.append(path)
            else:
                path += '->'  # 这里需要注意, 在非叶子节点的情况下要先在path后加上'->'
                dfs(root.left, path)
                dfs(root.right, path)

        res = []
        dfs(root, '')
        return res

