from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        #  当前index出可以走到的最大距离
        max_distance = 0

        for i in range(len(nums)):
            # 如果当前索引大于max_distance, 说明没法到达当前索引, 必然也到不了终点
            if i > max_distance:
                return False
            # 迭代更新max_distance
            max_distance = max(max_distance, nums[i] + i)

        return True
