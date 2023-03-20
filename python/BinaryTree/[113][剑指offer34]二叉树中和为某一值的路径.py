from typing import List
from CreateTree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def getPathSum(root: TreeNode, curpath: List[int]):
            if not root:
                return []   # 越过叶节点, 返回空列表
            if not root.left and not root.right:    # 到达叶节点,
                if root.val + sum(curpath) == target:   # 判断当前路径和+当前节点值是否等于目标值
                    return [curpath +[root.val]] # 等于目标值, 返回该路径列表
            # 在左右子树递归, 当前节点的结果为左右子树的返回列表拼接
            return getPathSum(root.left, curpath +[root.val]) + getPathSum(root.right, curpath +[root.val])

        return getPathSum(root, [])