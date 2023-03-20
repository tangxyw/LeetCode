from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 二分法
        # https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/solution/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/
        # 双指针
        left, right = 0, len(nums) - 1
        while left <= right:  # 加=是为了[0]这个特殊case
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1

        return left
