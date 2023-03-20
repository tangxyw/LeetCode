from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-ii-by-leetcode-soluti-f7uh/
        # 动态规划, 注意求的是组合数不是排列数, 所以遍历的嵌套顺序要改变, 详见上面链接

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]