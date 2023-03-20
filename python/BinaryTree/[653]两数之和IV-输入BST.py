from CreateTree import TreeNode

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.set = set()    # 存放已经得到的节点值集合
        self.res = False
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            if k - root.val in self.set:    # 如果已经满足条件, 停止递归
                self.res = True
                return
            self.set.add(root.val)  # 将当前节点值加入节点值集合
            inorder(root.right)
        inorder(root)
        return self.res