from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # 顺子条件
        # 1. 最大排面 - 最小排面 < 5
        # 2. 除了大小王(0)外不能有重复值

        s = set()
        max_val = 0  # 最大牌面
        min_val = 14  # 最小牌面

        for num in nums:
            if num == 0:    # 不考虑大小王
                continue
            if num in s:    # 有重复牌必然不是顺子
                return False
            # 更新最大最小牌面
            max_val = max(max_val, num)
            min_val = min(min_val, num)
            s.add(num)

        # 最大排面 - 最小排面 < 5才是顺子
        return max_val - min_val < 5
