from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1

        left = 0  # 左指针, 它左边的数字都是唯一值
        right = 1  # 右指针, 它用来判断是否和左指针指向的数值相等, 不相等就把右指针指向的数字赋值到左指针后面
        while right < len(nums):
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1  # 赋值完成后左指针右移一位
            right += 1  # 右指针一直右移

        return left + 1