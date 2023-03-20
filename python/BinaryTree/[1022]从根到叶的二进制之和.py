from typing import List
from CreateTree import TreeNode

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, sum: int):
            # 前序遍历
            if not root:
                return
            sum = (sum << 1) + root.val # 每条路径上的和, 用到了位运算
            if root.left is None and root.right is None:    # 到达叶节点
                self.res += sum # 将路径和加到总和上
            # 向下递归
            dfs(root.left, sum)
            dfs(root.right, sum)

        self.res = 0
        dfs(root, 0)
        return self.res