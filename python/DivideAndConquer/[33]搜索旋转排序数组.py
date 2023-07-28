from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[0] == target:
                return mid
            if nums[0] <= nums[mid]:  # mid位置在原始数组“左侧”部分
                if nums[0] <= target < nums[mid]:  # target也在这一部分
                    right = mid - 1
                else:  # # target也在这一部分
                    left = mid + 1
            else:  # mid位置在原始数组“右侧”部分
                if nums[mid] < target <= nums[len(nums)-1]:  # # target也在这一部分
                    left = mid + 1
                else:  # # target也在这一部分
                    right = mid - 1

        return -1
