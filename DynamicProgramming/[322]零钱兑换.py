from typing import List


class Solution(object):
    """
    给定不同面额的硬币coins和一个总金额amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
    你可以认为每种硬币的数量是无限的.
    例如:
    输入：coins = [1, 2, 5], amount = 11
    输出：3
    解释：11 = 5 + 5 + 1

    输入：coins = [2], amount = 3
    输出：-1

    输入：coins = [1], amount = 0
    输出：0
    """

    @staticmethod
    def coinChange_1(coins: List[int], amount: int) -> int:
        """
        递归解法
        :param coins: 硬币种类列表
        :param amount: 要凑成的金额
        :return: 最少硬币数
        """

        def dp(n):
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('inf')  # 求最小值, 所以初始化为正无穷
            for coin in coins:
                subproblem = dp(n - coin)  # 求解子问题
                if subproblem == -1: continue  # 非常重要, 若子问题无解, 则跳到下一个硬币, 不更新res
                res = min(res, 1 + subproblem)  # 在所有有解的子问题中选择最小的方案
            if res == float('inf'):
                return -1  # 若没有有解的子问题, 返回-1
            else:
                return res  # 存在有解的子问题, 返回最小的子问题的值

        return dp(amount)

    @staticmethod
    def coinChange_2(coins: List[int], amount: int) -> int:
        """
        带备忘录的递归解法
        时间复杂度O(amount*len(coins))
        :param coins: 硬币种类列表
        :param amount: 要凑成的金额
        :return: 最少硬币数
        """
        memo = {}   # 初始化备忘录
        def dp(n):
            if n in memo: return memo[n]  # 首先在备忘录里查询
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('inf')  # 求最小值, 所以初始化为正无穷
            for coin in coins:
                subproblem = dp(n - coin)  # 求解子问题
                if subproblem == -1: continue  # 非常重要, 若子问题无解, 则跳到下一个硬币, 不更新res
                res = min(res, 1 + subproblem)  # 在所有有解的子问题中选择最小的方案

            if res == float('inf'):
                memo[n] = -1  # 若没有有解的子问题, 在备忘录中记录-1
            else:
                memo[n] = res  # 存在有解的子问题, 在备忘录中记录最小的子问题的值
            return memo[n]
        return dp(amount)

    @staticmethod
    def coinChange_3(coins: List[int], amount: int) -> int:
        """
        动态规划解法
        时间复杂度O(amount*len(coins))
        :param coins: 硬币种类列表
        :param amount: 要凑成的金额
        :return: 最少硬币数
        """
        # 初始化dp table, 长度为amount+1, 每一项值为正无穷
        dp = [float('inf') for i in range(amount+1)]
        # base case
        dp[0] = 0
        for n in range(1, amount+1):  # 从第1项开始递推dp table
            for coin in coins:  # 遍历每一种硬币
                if n < coin: continue  # 如果问题规模小于当前硬币面值, 进入下一轮循环
                else: dp[n] = min(dp[n], dp[n-coin]+1)  # dp状态转移方程
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

if __name__ == '__main__':
    # print(Solution.coinChange_1([1, 2, 5], 12))     # 3
    # print(Solution.coinChange_1([5, 6], 132))    # 22

    print(Solution.coinChange_2([1, 2, 5], 12))     # 3
    print(Solution.coinChange_2([5, 6], 132))    # 22

    print(Solution.coinChange_3([1, 2, 5], 12))     # 3
    print(Solution.coinChange_3([5, 6], 132))    # 22
