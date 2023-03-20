from CreateTree import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def getLeftSum(root, direction):
            # direction为方向因子, 左子树1右子树0
            if not root:    # 到底了, 返回0
                return 0
            if not root.left and not root.right:    # 到达根节点, 返回节点值和方向因子的乘机
                return root.val*direction
            return getLeftSum(root.left, 1)+getLeftSum(root.right, 0)   #结果为左右子树递归结果的和
        return getLeftSum(root, 0)  # 只有一个根节点, 也返回0