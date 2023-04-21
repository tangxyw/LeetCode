from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(start: int, end: int) -> None:
            if start >= end:
                return

            # 在区间[start, end]内随机选取一个点作为pivot, 放到start位置
            t = random.randint(start, end)
            pivot = nums[t]
            nums[t], nums[start] = nums[start], nums[t]

            i, j = start, end

            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1  # 左移j, 直到j右边都>=pivot, j停在<pivot的位置上
                while i < j and nums[i] <= pivot:
                    i += 1  # 右移i, 直到i左边都<=pivot, i停在>pivot的位置上
                nums[i], nums[j] = nums[j], nums[i]  # 交换i, j元素进入下一轮迭代
            # 上述迭代完成后, i和j指向的位置相同, 该位置元素<pivot(因为先移动j后移动i), 交换它们的位置, 使得pivot放在了正确的升序位置
            nums[start], nums[i] = nums[i], nums[start]

            # 此时,索引为i前面的元素都<=nums[i], 后面的算都>=nums[i], 即nums[i]已经放到了正确的升序位置上
            # 向下递归
            quicksort(start, i - 1)
            quicksort(i + 1, end)

        quicksort(0, len(nums) - 1)

        return nums
