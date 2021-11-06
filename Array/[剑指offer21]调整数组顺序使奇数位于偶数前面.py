from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 0  # 指针
        for i in range(n):
            if nums[i] % 2 == 1:  # 当位置i为奇数时
                nums[i], nums[p] = nums[p], nums[i]  # 交换i和p位置的数字
                p += 1  # p右移, 保证p左侧都是奇数

        return nums
