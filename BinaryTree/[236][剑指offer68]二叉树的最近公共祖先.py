from CreateTree import TreeNode


class Solution:
    # 此题画出递归树后较好理解
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 后序遍历
        # base case
        if not root or (root == p) or (root == q):
            # 当前节点为None时, 返回None
            # 当前节点为p或q时, 返回p或q
            return root
        # 在左右子树中递归
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:  # 左子树递归结果为空, 说明p和q都不在左子树内, 此时返回右子树递归结果
            return right
        if not right:  # 反之, 返回左子树递归结果
            return left
        if left and right:  # 若p和q分别在左右子树内, 则当前节点为最近公共祖先(由后序遍历保证)
            return root
