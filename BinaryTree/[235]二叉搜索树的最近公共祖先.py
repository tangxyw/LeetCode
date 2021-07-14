from CreateTree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        while True:
            if p.val < res.val and q.val < res.val:  # p和q的val都比当前节点val小, 下一步在当前节点左子树中寻找
                res = res.left
            elif p.val > res.val and q.val > res.val:  # p和q的val都比当前节点val大, 下一步在当前节点右子树中寻找
                res = res.right
            else:  # 这时p.val <= res.val <= q.val, 此时要么当前节点是p/q之一, 要么p和q分别在当前节点的左右子树中.所以当前节点就是所求, 结束循环, 返回res
                break
        return res
