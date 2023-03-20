from .CreateTree import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:  # 当前节点为空, 返回0, 注意这里解决的是只有一个子节点, 当递归到空的那个节点时的情况
                return 0
            total = prevTotal * 10 + root.val  # 当前值乘10再加当前节点值
            if not root.left and not root.right:  # 到达叶子节点, 就把当前路径值返回给上层递归
                return total
            else:  # 非叶子节点, 向左右子树递归, 返回它们的和
                return dfs(root.left, total) + dfs(root.right, total)

        # 从根节点开始递归, 返回结果
        return dfs(root, 0)
