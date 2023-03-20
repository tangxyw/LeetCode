class Solution(object):
    """
    求解斐波那契数列的第N项
    """

    @staticmethod
    def fib_1(N: int) -> int:
        """
        递归解法,
        时间复杂度O(2^n)
        """
        if N < 1: return 0
        if N == 1 or N == 2:
            return 1
        res = Solution.fib_1(N - 1) + Solution.fib_1(N - 2)
        return res

    @classmethod
    def fib_2(cls, N: int) -> int:
        """
        带备忘录的递归解法,
        时间复杂度O(n)
        """
        if N < 1: return 0
        memo = {}  # 定义备忘录

        def helper(n):
            if n == 1 or n == 2:
                return 1
            if n in memo.keys():  # 判断fib(n)是否已经被记录了
                return memo[n]
            memo[n] = helper(n - 1) + helper(n - 2)
            return memo[n]

        return helper(N)

    @staticmethod
    def fib_3(N: int) -> int:
        """
        动态规划解法
        时间复杂度O(n)
        """
        if N < 1:
            return 0
        if N == 1 or N == 2:
            return 1
        dp = [0] * (N+1)    # dp table
        dp[1] = dp[2] = 1
        for i in range(3, N+1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[N]


if __name__ == '__main__':
    print('fib_1(10) = ', Solution.fib_1(10))
    print('fib_2(10) = ', Solution.fib_2(10))
    print('fib_3(10) = ', Solution.fib_3(10))
