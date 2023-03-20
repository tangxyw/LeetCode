from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针
        left = 0    # 左指针左边的元素都不等于val
        for right in range(len(nums)):  # 遍历右指针
            if nums[right] != val:  # 右指针指向的值不等于val, 就放在左指针的位置上, 相当于把所有不等于val的值都「挤」到前面
                nums[left] = nums[right]
                left += 1

        return left
