from CreateTree import TreeNode

class Solution:
    # 此题画出递归树后较好理解
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (root is None) or (root == p) or (root == q):
            # 当前节点为None时, 返回None
            # 当前节点为p或q时, 返回p或q
            return root
        # 在左右子树中递归
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right,p, q)
        if left is None:    # 左子树递归结果为空, 说明p和q都不在左子树内, 此时返回右子树递归结果
            return right
        elif right is None: # 反之, 返回左子树递归结果
            return left
        elif left and right:  # 若p和q分别在左右子树内, 则当前节点为最近公共祖先(由dfs保证)
            return root