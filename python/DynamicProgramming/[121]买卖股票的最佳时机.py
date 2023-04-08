from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_bonus = 0   # 最大收益
        min_price = prices[0]   # 当前索引之前的最小价格

        for i in range(1, len(prices)): # 从第2个元素开始遍历
            max_bonus = max(max_bonus, prices[i] - min_price)   # 更新最大收益
            min_price = min(min_price, prices[i])   # 更新最小价格

        return max_bonus
