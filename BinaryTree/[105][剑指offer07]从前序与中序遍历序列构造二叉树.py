from typing import List
from CreateTree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder_left, preorder_right, inorder_left, inorder_right):
            """
            4个参数分别是前序列表的区间指针和中序列表的区间指针
            """
            # base case
            if preorder_left > preorder_right:
                return None

            # 前序列表: [根, 左子树, 右子树]
            # 中序列表: [左子树, 根, 右子树]

            # 前序列表的第一个元素为根节点值
            root_val = preorder[preorder_left]
            # 取得根节点在中序列表的索引
            root_idx = inorder.index(root_val)

            # 左子树节点数量
            size_left_subtree = root_idx - inorder_left

            # 左子树4个参数
            l_preorder_left = preorder_left + 1
            l_preorder_right = preorder_left + size_left_subtree
            l_inorder_left = inorder_left
            l_inorder_right = root_idx - 1

            # 右子树4个参数
            r_preorder_left = preorder_left + size_left_subtree + 1
            r_preorder_right = preorder_right
            r_inorder_left = root_idx + 1
            r_inorder_right = inorder_right

            # 构造当前根节点, 递归构造左右子树
            node = TreeNode(root_val)
            node.left = helper(l_preorder_left, l_preorder_right, l_inorder_left, l_inorder_right)
            node.right = helper(r_preorder_left, r_preorder_right, r_inorder_left, r_inorder_right)

            return node

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)