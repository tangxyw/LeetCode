from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:  # 将nums[i]放到"正确"的位置上, 即nums[nums[i] - 1]上,
                # while条件不满足时, 要么当前就是nums[i]的正确位置, 要么正确位置(不是当前位置)已经是nums[i]了

                # 注意不能写成nums[i], nums[nums[i]- 1] = nums[nums[i] - 1], nums[i]
                # 原因见https://stackoverflow.com/questions/68152730/understand-python-swapping-why-is-a-b-b-a-not-always-equivalent-to-b-a-a
                p = nums[i]
                nums[p - 1], nums[i] = nums[i], nums[p - 1]

        # 返回所有不在正确位置的那些元素
        return [nums[i] for i in range(len(nums)) if nums[i] - 1 != i]
