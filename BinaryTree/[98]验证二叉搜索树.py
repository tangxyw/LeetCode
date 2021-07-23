from CreateTree import TreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root: TreeNode, lower=-float('inf'), upper=float('inf')) -> bool:
            # lower和upper为上下界, 默认值为正负无穷
            # 思路是上层节点把上下界的信息通过递归传向下层节点, 下层节点得到结果向上返回
            if not root:
                return True
            if root.val <= lower or root.val >= upper:  # 当前节点值不在上下界内, 返回False
                return False
            # 递归左子树, 左子树根节点值的下界继承自它的父节点, 上界为父节点值
            left = helper(root.left, lower, root.val)
            # 递归右子树, 右子树根节点值的下界为父节点值, 上界继承自它的父节点
            right = helper(root.right, root.val, upper)
            return left and right

        return helper(root)