from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # 牌中的最大最小值
        min_num = 14
        max_num = 0
        # 记录牌中出现的数字
        repeat = set()

        for num in nums:
            if num > 0:  # 只考虑不是大小王的牌
                # 更新牌的最大值最小值
                min_num = min(num, min_num)
                max_num = max(num, max_num)
                if max_num - min_num >= 5:  # 最大值-最小值>=5, 不可能组成顺子
                    return False
                if num in repeat:  # 牌已经出现过
                    return False
                repeat.add(num)

        return True
