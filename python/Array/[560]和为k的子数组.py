from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_count = dict()  # 前缀和:出现次数
        pre_count[0] = 1    # 前缀和本身为k的特殊情况
        pre = 0  # 记录当前前缀和
        res = 0  # 最终结果

        for num in nums:
            pre += num  # 更新前缀和
            if pre_count.get(pre - k):  # pre-k在pre_count中, 说明有和为k的子数组
                res += pre_count[pre - k]  # 之前pre-k出现几次, 结果就加几次
            pre_count[pre] = pre_count.get(pre, 0) + 1  # 前缀和出现次数+1

        return res

