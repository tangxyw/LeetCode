from typing import Optional
from CreateTree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        if not root:
            return False
        # 叶节点
        if not root.left and not root.right:
            return targetSum == root.val
        # 递归左右子树
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right
