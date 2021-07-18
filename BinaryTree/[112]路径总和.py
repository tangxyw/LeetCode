from CreateTree import TreeNode

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def getPath(root: TreeNode, sumpath):
            """返回根节点到当前节点的路径和"""
            if not root:
                return
            if not root.left and not root.right:    # 当到达叶节点时, 判断路径和是否和目标值相等
                if sumpath+root.val == targetSum:
                    self.flag = True
                return
            getPath(root.left, sumpath+root.val)
            getPath(root.right, sumpath+root.val)

        if not root:
            return False
        self.flag = False
        getPath(root, 0)
        return self.flag