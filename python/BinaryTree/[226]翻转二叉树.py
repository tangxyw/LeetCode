from typing import List
from CreateTree import TreeNode

class Solution:
    @staticmethod
    def invertTree(root: TreeNode) -> TreeNode:
        if not root:
            return root
        # 交换左右子树
        root.left, root.right = root.right, root.left
        # 递归
        root.left = Solution.invertTree(root.left)
        root.right = Solution.invertTree(root.right)
        return root
