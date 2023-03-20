from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分查找
        # 双指针
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2  # 当前数组长度为偶数时, mid靠近left
            if nums[mid] < nums[right]:  # 中间位置元素小于右指针元素, 最小值在mid左边
                right = mid  # mid也可能为最小值
            elif nums[mid] > nums[right]:  # 中间位置元素大于右指针元素, 最小值在右边
                left = mid + 1  # mid不可能为最小值
            elif nums[mid] == nums[right]:  # 中间位置元素等于右指针元素, 不能确定最小值在哪个区间
                right -= 1  # 只能确定nums[right]不是唯一的最小值, 右指针左移一格继续下一轮迭代

        # 最终left和right指向同一个位置, 任选一个返回
        return nums[left]
