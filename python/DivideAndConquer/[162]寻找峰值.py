from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 二分法
        n = len(nums)
        left = 0
        right = n - 1

        def get(i: int) -> int:
            """辅助函数, 处理索引边界"""
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        while left <= right:
            if left == right:
                return left
            mid = (right - left) // 2 + left
            if get(mid - 1) < get(mid) > get(mid + 1):  # 找到峰值返回
                return mid
            elif get(mid) < get(mid + 1):  # 上坡, 峰值在右侧
                left = mid + 1
            else:  # 下坡, 峰值在左侧
                right = mid - 1
