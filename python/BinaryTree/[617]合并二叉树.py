from typing import List
from CreateTree import TreeNode


class Solution:
    @staticmethod
    def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        # 实际是前序遍历
        merged = TreeNode(root1.val + root2.val)
        merged.left = Solution.mergeTrees(root1.left, root2.left)
        merged.right = Solution.mergeTrees(root1.right, root2.right)
        return merged