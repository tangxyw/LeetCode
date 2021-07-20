from typing import List
from CreateTree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  # 消费完前序和中序列表, 递归完成
            return
        root_val = preorder[0]  # 前序列表的第一个元素为根节点值
        root_idx = inorder.index(root_val)  # 根节点值在中序列表的索引, 注意这个索引值也是左子树节点总数

        inorder_left = inorder[0:root_idx]  # 中序列表中的左子树, 注意切片操作不会报错, 如左边界大于右边界会返回[]
        inorder_right = inorder[root_idx + 1:]  # 中序列表中的右子树

        preorder_left = preorder[1:root_idx + 1]  # 前序列表的左子树(利用root_idx的性质)
        preorder_right = preorder[root_idx + 1:]  # 前序列表的右子树

        node = TreeNode(root_val)
        node.left = self.buildTree(preorder_left, inorder_left)  # 递归构建左子树
        node.right = self.buildTree(preorder_right, inorder_right)  # 递归构建右子树

        return node