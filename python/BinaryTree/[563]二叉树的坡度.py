from CreateTree import TreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def getSum(root: TreeNode):
            """返回每个节点的左子树+右子树+自身的val和"""
            if not root:  # 到底了返回0
                return 0
            left_sum = getSum(root.left)  # 递归左子树
            right_sum = getSum(root.right)  # 递归右子树
            self.res += abs(left_sum - right_sum)  # 计算当前节点坡度, 累加到res上
            return root.val + left_sum + right_sum

        self.res = 0
        getSum(root)
        return self.res
