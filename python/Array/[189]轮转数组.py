from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n  # k可能大于n, 数组向右移动n步又回到了起始位置

        reverse(0, n - 1)  # 反转整个数组
        reverse(0, k - 1)  # 反转前k个元素
        reverse(k, n - 1)  # 反转后n-k个元素
