from CreateTree import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: # 直到叶子节点两棵树都相同
            return True
        elif (p and not q) or (not p and q):    # p和q有一个为空另一个不为空, 不相同
            return False
        else:   # P和q都不为空
            if p.val != q.val:  # p和q的val不等, 不相同
                return False
            else:   # p和q的val相等, 继续递归
                left_flag = self.isSameTree(p.left, q.left) # 比较p和q的左子树
                right_flag = self.isSameTree(p.right, q.right)  # 比较p和q的右子树
                if left_flag and right_flag:    # 左右子树都相同
                    return True
                else:
                    return False