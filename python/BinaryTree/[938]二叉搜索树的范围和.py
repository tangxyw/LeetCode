from typing import List
from CreateTree import TreeNode


class Solution:
    @staticmethod
    def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
        def rangeSum(root: TreeNode, low: int, high: int) -> int:
            if root is None:
                return
            if root.val <= high and root.val >= low:
                res.append(root.val)
                rangeSum(root.left, low, high)
                rangeSum(root.right, low, high)

            elif root.val > high:
                rangeSum(root.left, low, high)

            elif root.val < low:
                rangeSum(root.right, low, high)
        res = []
        rangeSum(root, low, high)
        sum = 0
        for i in res:
            sum += i
        return sum


if __name__ == '__main__':
    from CreateTree import list_creat_tree
    llist = [10, 5, 15, 3, 7, None, 18]
    root = list_creat_tree(None, llist, 0)
    print(Solution.rangeSumBST(root, 7, 15))

