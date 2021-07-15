from CreateTree import TreeNode

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # BST的中序遍历结果是严格单调递增的
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            self.res = min(self.res, root.val-self.cur) # 更新res
            self.cur = root.val # 记住当前节点值
            inorder(root.right)

        self.res = float("inf") # 记录当前最小差, 初值赋值为正无穷
        self.cur = float("-inf")    # 当前节点值初值赋值为负无穷, 确保遍历第一个值后的res逻辑无误
        inorder(root)

        return self.res