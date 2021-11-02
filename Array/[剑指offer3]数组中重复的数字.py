from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:  # 遍历nums
            if nums[i] == i:  # nums[i]在正确的位置上, 进入下一个位置的迭代
                i += 1
                continue
            j = nums[i]  # 否则, 记位置i的数字为j
            if nums[i] == nums[j]:  # 位置i的数字与位置j的数字相同, 则找到题目所求
                return nums[i]
            nums[i], nums[j] = nums[j], nums[i]  # 否则, 交换位置i和位置j的数字, 即把j放到了正确的位置上, 再进入下一轮迭代(i未改变)
