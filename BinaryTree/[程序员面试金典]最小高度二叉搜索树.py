from typing import List
from CreateTree import TreeNode


class Solution:
    @staticmethod
    def sortedArrayToBST(nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return

        median_index = len(nums) // 2   # 中位数索引
        median = nums[median_index]
        lower = nums[:median_index] # 小于中位数的值构造左子树
        higher = nums[(median_index + 1):]  # 大于中位数的值构造右子树
        root = TreeNode(median)
        root.left = Solution.sortedArrayToBST(lower)
        root.right = Solution.sortedArrayToBST(higher)

        return root


if __name__ == '__main__':
    nums = [-10, -7, 0, 5, 9]
    root = Solution.sortedArrayToBST(nums)
