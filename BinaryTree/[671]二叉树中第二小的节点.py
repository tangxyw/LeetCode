from CreateTree import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if not root:  # 到底了, 未找到节点值大于根节点值的节点, 返回-1
                return -1
            if root.val > self.min1:  # 当前节点的值比根节点值大, 说明第二小值不会在以当前节点为根的子树里, 停止递归
                return root.val
            left = dfs(root.left)  # 递归左子树
            right = dfs(root.right)  # 递归右子树
            if left == -1:  # 左子树里没找到, 返回右子树的结果
                return right
            if right == -1:  # 右子树里没找到, 返回左子树的结果
                return left
            return min(left, right)  # 左右子树都找到了比根节点值大的, 返回最小的那个

        self.min1 = root.val
        return dfs(root)