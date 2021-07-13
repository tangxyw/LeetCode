from typing import List
from CreateTree import TreeNode

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # 前序遍历
        if not root:
            return False
        self.val = root.val
        self.flag = True
        def preorder(root: TreeNode):
            if not root:
                return
            if self.flag == False:  # 已经找到不一样的值, 无需再递归了
                return
            if root.val != self.val:  # 找到不一样的值, 改变flag
                self.flag = False
                return
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return self.flag