from CreateTree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True

        def getDepth(root):
            """返回以节点为根节点的子树的深度, 判断左右子树的深度差"""
            if not root:
                return 0
            if not self.flag:
                return
            left_depth = getDepth(root.left)
            right_depth = getDepth(root.right)
            print(left_depth, right_depth)
            if abs(left_depth - right_depth) > 1:
                # print(left_depth, right_depth)
                self.flag = False
            return max(left_depth, right_depth) + 1

        getDepth(root)
        return self.flag