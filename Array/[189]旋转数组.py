from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n   # k可能大于n, 数组向右移动n步又回到了起始位置

        nums.reverse()  # 反转数组

        # 反转前k个元素组成的子数组
        left = 0
        right = k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # 再反转后n-k个元素组成的子数组
        left = k
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1