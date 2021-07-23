from CreateTree import TreeNode

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # BST的中序遍历为递增序列
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            if self.k == 1:
                return root.val
            self.k -= self.k
            print(root.val)
            inorder(root.right)

        self.k = k
        return inorder(root)