from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 利用dict, 只需遍历一次数组
        d = dict()  # k为数组值v为值的索引
        for index in range(len(nums)):  # 遍历数组
            if target - nums[index] in d:  # 判断target-当前值是否在数组中
                return [index, d[target - nums[index]]]  # 如果在, 返回索引
            d[nums[index]] = index  # 不在, 将当前值和索引加入字典
