from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            if left == right:  # 到了数组边界
                return left
            mid = (right - left) // 2 + left
            if nums[mid] < nums[mid + 1]:  # mid右侧的数更大，右侧区间必存在峰值
                left = mid + 1
            elif nums[mid - 1] < nums[mid]:  # mid比mid+1大, 且也比mid-1大, mid就是峰值
                return mid
            elif nums[mid - 1] > nums[mid]:  # mid左侧的数更大, 左侧区间必存在峰值
                right = mid - 1
