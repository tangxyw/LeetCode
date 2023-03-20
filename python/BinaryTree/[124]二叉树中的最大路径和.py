from CreateTree import TreeNode

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root: TreeNode) -> int:
            """返回以root为起点(向下)的最大路径, 并计算以root节点为转折节点的最大路径"""
            if not root:    # 越过叶节点, 返回0
                return 0
            left = max(helper(root.left), 0)    # 向左子树递归, 如果结果小于0, 则取0, 相当于从左子树截断
            right = max(helper(root.right), 0)  # 同上
            self.maxpath = max(self.maxpath, left+right+root.val)   # left+right+root.val为以root为转折点的最大路径(可能为负值)
            return max(left, right) + root.val  # 在左右子树递归结果中选择大的那个, 再加上root本身的值作为返回值, 注意这个值可能为负, 不过在向上递归后会当作0

        self.maxpath = float('-inf')
        helper(root)
        return self.maxpath