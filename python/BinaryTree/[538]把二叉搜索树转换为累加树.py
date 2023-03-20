from CreateTree import TreeNode

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 逆序的中序遍历二叉搜索树, 得到的是递减序列
        def reverserInorder(root: TreeNode):
            if not root:
                return
            reverserInorder(root.right)
            self.cur_count += root.val
            root.val = self.cur_count
            reverserInorder(root.left)

        self.cur_count = 0
        reverserInorder(root)
        return root
