from .CreateTree import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def issysmmetric(left, right):
            """比较对称位置的两个节点"""
            # 对称位置都为空
            if not left and not right:
                return True
            # 对称位置一个为空另一个不为空
            if (not left and right) or (not right and left):
                return False
            # 对称位置节点值不相等
            if left.val != right.val:
                return False
            # 向下一层递归, 有两对对称位置
            return issysmmetric(left.left, right.right) and issysmmetric(left.right, right.left)

        if not root:
            return True
        return issysmmetric(root.left, root.right)
