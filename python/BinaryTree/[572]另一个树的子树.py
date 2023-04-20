from CreateTree import TreeNode


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSametree(p: TreeNode, q: TreeNode) -> bool:
            """判断两棵树是否完全相同"""
            if not p and not q:  # 都到底了 且 都为空, 相同
                return True
            if not p or not q:  # p和q有一个为空另一个不为空, 不相同
                return False
            # 节点值相等 且 左子树完全相同 且 右子树完全相同 → p和q完全相同
            return p.val == q.val and isSametree(p.left, q.left) and isSametree(p.right, q.right)

        # 遍历root的每一个节点, 判断subRoot是否为root的子树
        if not root and not subRoot:  # root和subRoot都为空
            return True
        if not root or not subRoot:  # root和subRoot有一个不为空
            return False
        # 向root的左右子树递归, subRoot是root.left的子树 或 subRoot是root.right的子树 或 root和subRoot完全相同 → subRoot为root的子树
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or isSametree(root, subRoot)
