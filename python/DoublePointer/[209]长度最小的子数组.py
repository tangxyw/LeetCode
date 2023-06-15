from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        res = float('inf')

        # 滑动窗口
        s = 0  # 子数组和
        while right < n:
            s += nums[right]
            while s >= target:
                # 每当s>=target时, 更新res
                res = min(res, right - left + 1)
                s -= nums[left]
                left += 1  # 左端点右移
            right += 1  # 右端点右移

        # 可能没有>=target的子数组
        return res if res < float('inf') else 0




