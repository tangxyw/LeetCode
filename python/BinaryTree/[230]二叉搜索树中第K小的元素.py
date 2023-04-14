from CreateTree import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # BST的中序遍历为递增序列
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            inorder(root.right)

        self.k = k
        self.res = None
        inorder(root)

        return self.res
