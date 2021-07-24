from CreateTree import TreeNode

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return None
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            sumpath = helper(root.left) + helper(root.right) + root.val
            self.maxpath = max(self.maxpath, sumpath)
            inorder(root.right)

        def helper(root: TreeNode) -> int:
            """返回以root节点为转折节点的最大路径"""
            if not root:
                return 0
            return max(helper(root.left), helper(root.right)) + root.val

        self.maxpath = float('-inf')
        inorder(root)
        return self.maxpath