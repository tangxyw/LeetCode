from CreateTree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root: TreeNode) -> (bool, int):
            """返回以节点为根节点的子树是否为高度平衡树, 和当前子树深度"""
            # base case
            if not root:
                return True, 0
            # 后序遍历
            left_flag, left_depth = helper(root.left)
            right_flag, right_depth = helper(root.right)
            # 当前左右子树都为高度平衡树, 且左右子树高度差<=1时, 当前子树为高度平衡树
            return left_flag and right_flag and abs(left_depth - right_depth) <= 1, max(left_depth, right_depth) + 1

        # 只返回第一个bool值即可
        return helper(root)[0]
