from CreateTree import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 注意此题与 572.另一个树的子树 的区别, 一个是子树, 一个是子结构
        if not A or not B:  # A为空表示到底了也没找到相同子结构, 返回False; B为空根据题意返回False
            return False
        # 当以A为根节点的子树包含结构B 或 以A的左子树为根节点的子树包含结构B 或 以A的右子树为根节点的子树包含结构B → A包含结构B
        return self.isSub(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isSub(self, Node_inA: TreeNode, B: TreeNode) -> bool:
        """判断以Node_inA为根节点的子树是否包含结构B"""
        if not B:  # B为空表示递归到B底部了没找到不一样的, 返回True
            return True
        if not Node_inA:  # B不为空A为空表示A到底了, 返回False
            return False
        # 当Node_inA和B的节点值相等 且 Node_inA的左子树包含B的左子树结构 且 Node_inA的右子树包含B的右子树结构 → 以Node_inA为根节点的子树是否包含结构B
        return Node_inA.val == B.val and self.isSub(Node_inA.left, B.left) and self.isSub(Node_inA.right, B.right)