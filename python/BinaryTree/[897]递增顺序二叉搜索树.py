from typing import List
from CreateTree import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            self.cur_node.right = TreeNode(root.val)    # 指针节点的右子树初始化
            self.cur_node = self.cur_node.right   # 指针节点指向右子节点
            inorder(root.right)

        dummy = TreeNode(-1)    # 用哑节点初始化, 在递归中不改变此指针, 起到锚的作用.
        self.cur_node = dummy   # 初始化指针节点
        inorder(root)
        return dummy.right