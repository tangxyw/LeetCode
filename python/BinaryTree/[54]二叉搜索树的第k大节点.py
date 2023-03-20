from typing import List
from CreateTree import TreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # BST的中序遍历"左根右"是严格递增序列, 而"右根左"的是严格递减序列, 取这个序列的第k个元素即为结果
        def inorder(root: TreeNode):
            if not root:
                return
            if self.k == 0:  # k等于0说明已经得到结果, 递归可以结束了
                return
            inorder(root.right)  # 遍历右子树
            self.k -= 1  # 每遍历一次根, k就减1
            if self.k == 0:  # k等于0时, 取根的val, 返回
                self.res = root.val
                return
            inorder(root.left)  # 遍历左子树

        # 在递归外初始化, 必须用成员变量
        self.res = None
        self.k = k

        inorder(root)
        return self.res