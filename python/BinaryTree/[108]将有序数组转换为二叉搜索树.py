from typing import List, Optional
from CreateTree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            mid = start + (end - start) // 2
            node = TreeNode(nums[mid])
            node.left = helper(start, mid - 1)
            node.right = helper(mid + 1, end)

            return node

        return helper(0, len(nums) - 1)
