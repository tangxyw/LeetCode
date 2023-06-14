from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分查找
        # 双指针
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2  # 当前数组长度为偶数时, mid靠近left
            if nums[mid] < nums[-1]:  # 中间位置元素小于nums最右元素, 最小值在mid左边
                right = mid  # mid也可能为最小值
            else:  # 中间位置元素大于右指针元素, 最小值在右边
                left = mid + 1  # mid不可能为最小值

        # 最终left和right指向同一个位置, 任选一个返回
        return nums[left]
