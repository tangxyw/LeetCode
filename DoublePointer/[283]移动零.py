from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针
        j = 0  # 记录非0元素的指针
        for i in range(len(nums)):  # 用指针i遍历nums
            if nums[i]:  # i位置的元素不为0时
                nums[j] = nums[i]  # 把位置的非0数字放到位置j上
                j += 1  # j右移1步

        # 上面遍历完成后, j指向的位置的前面都是非0数字, 后面都应该被赋值为0
        for k in range(j, len(nums)):
            nums[k] = 0
