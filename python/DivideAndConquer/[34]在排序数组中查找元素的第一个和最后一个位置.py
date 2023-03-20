from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(left, right) -> List[int]:
            # base case
            if nums[left] == nums[right] == target:  # 整个区间都是target
                return [left, right]
            if target < nums[left] or target > nums[right]:  # target不在区间内
                return [-1, -1]

            # 分成左右两个区间递归
            mid = (right - left) // 2 + left
            left = helper(left, mid)
            right = helper(mid + 1, right)

            if left[0] == -1 or right[0] == -1:  # 至少有一个区间没有target
                return left if right[0] == -1 else right
            else:  # 两个区间都有target
                return [left[0], right[-1]]

        if not nums:
            return [-1, -1]
        return helper(0, len(nums) - 1)