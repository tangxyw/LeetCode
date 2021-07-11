from typing import List
from CreateTree import TreeNode


class Solution:
    @staticmethod
    def searchBST(root: TreeNode, val: int) -> TreeNode:
        if not root:
            return

        if root.val == val:
            return root
        elif root.val < val:
            return Solution.searchBST(root.right, val)
        elif root.val > val:
            return Solution.searchBST(root.left, val)