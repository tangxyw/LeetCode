from CreateTree import TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 前序遍历"根左右"
        def preorder(root: TreeNode):
            if not root:
                return
            if not root.left and not root.right:  # 到达叶子节点
                self.root1_res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        self.root1_res = []  # 存放root1的叶子节点值
        preorder(root1)

        # 逆序前序遍历"根右左"
        def invert_preorder(root: TreeNode):
            if not root:
                return
            if self.flag == False:  # flag已经变为False, 无需再递归了
                return
            if not root.left and not root.right:  # 到达叶子节点
                if not self.root1_res:  # 存放root1节点值的列表已经被消费空了, flag变为False
                    self.flag = False
                cur = self.root1_res.pop()  # 弹出root1_res最后一个元素, 并与当前叶子节点值作对比,
                if root.val != cur:  # 不相等, flag变为False
                    self.flag = False
            invert_preorder(root.right)
            invert_preorder(root.left)

        self.flag = True
        invert_preorder(root2)

        if self.root1_res or not self.flag:  # root1_res非空(未消费完), 或者flag为False
            return False
        else:
            return True