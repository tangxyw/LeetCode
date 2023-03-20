from .CreateTree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.helper(root) == -1:  # -1代表不平衡
            return False
        else:
            return True

    def helper(self, root: TreeNode) -> int:
        """返回以root为节点的子树的深度, 若子树不平衡, 则返回-1"""
        if not root:  # 叶子节点, 深度为0
            return 0
        left = self.helper(root.left)  # 递归左子树
        if left == -1:  # 左子树不平衡, 整颗子树也不平衡
            return -1
        right = self.helper(root.right)  # 右子树不平衡, 整颗子树也不平衡
        if right == -1:
            return -1
        if abs(left - right) <= 1:  # 左右子树深度差小于等于1, 为平衡子树
            return max(left, right) + 1  # 深度为左右子树中深度较大者+1
        else:
            return -1  # 深度差大于1, 不平衡
