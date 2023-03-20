from CreateTree import TreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 首先想到的是在遍历后一个节点的时候改变前一个节点的左右指针, 但是会在遍历root.left的时候把root.right改变, 而root.right还未遍历就被改变了
        # 所以要考虑前序遍历的逆序遍历, 即"右左根", 在遍历后一个节点的时候, 把后一个节点的右节点指向前一个节点, 而后一个节点的左右节点都已在之前完成遍历, 修改它们不受影响
        def rerversePreorder(root: TreeNode):
            if not root:
                return
            rerversePreorder(root.right)
            rerversePreorder(root.left)
            if self.pre:
                root.left = None
                root.right = self.pre
            self.pre = root

        self.pre = None
        rerversePreorder(root)
        return root