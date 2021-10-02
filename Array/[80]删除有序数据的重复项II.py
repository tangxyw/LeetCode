from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 更一般地, 考虑允许每个元素最多出现k次
        # [26]删除有序数据的重复项 也可归到此范式下
        def sovle(k):
            p = 0  # 指向最终位置的指针
            for num in nums:  # 遍历数组中所有元素
                if p < k:  # 前k个元素都是合法的
                    p += 1
                    continue
                elif nums[p - k] != num:  # 从第k+1个元素开始, 检查前面和ta隔着距离k的元素, 如果不等, 则将ta放到p的位置
                    nums[p] = num
                    p += 1  # 这时p往前走一步
            # p为最终位置
            return p

        return sovle(2)
