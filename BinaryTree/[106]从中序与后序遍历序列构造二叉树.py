from .CreateTree import TreeNode
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:  # 消费完中序和后序列表, 递归完成
            return

        root_val = postorder[-1]  # 后序遍历列表的最后一个元素是当前根节点的值
        root_idx = inorder.index(root_val)  # 根节点值在中序遍历列表的索引, 注意这个索引值相当于当前左子树的节点数量

        inorder_left = inorder[:root_idx]  # 左子树的中序遍历列表
        inorder_right = inorder[root_idx + 1:]  # 右子树的中序遍历列表

        postorder_left = postorder[:root_idx]  # 左子树的后序遍历列表(利用root_idx的性质)
        postorder_right = postorder[root_idx:-1]  # 右子树的后序遍历列表

        root = TreeNode(root_val)
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root
