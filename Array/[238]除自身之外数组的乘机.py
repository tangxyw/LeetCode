from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 结果集中每一个元素, 等于它的前缀积*后缀积
        res = [0] * n
        res[0] = 1

        # 前缀积
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # 后缀积, 需要一个变量R存储nums的后缀积
        R = 1
        for j in range(n - 1, -1, -1):  # 从后向前遍历
            res[j] = res[j] * R  # 前缀积*后缀积
            R *= nums[j]  # 更新后缀积

        return res
