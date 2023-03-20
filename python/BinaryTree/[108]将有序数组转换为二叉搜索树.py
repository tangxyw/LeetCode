from typing import List
from CreateTree import TreeNode

class Solution:
    @staticmethod
    def sortedArrayToBST(nums: List[int]) -> TreeNode:
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = Solution.sortedArrayToBST(nums[:mid])
        root.right = Solution.sortedArrayToBST(nums[(mid+1):])
        return root