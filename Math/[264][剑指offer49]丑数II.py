class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 动态规划
        # https://leetcode-cn.com/problems/ugly-number-ii/solution/san-zhi-zhen-fang-fa-de-li-jie-fang-shi-by-zzxn/
        dp = [0] * n
        dp[0] = 1  # base case
        p2, p3, p5 = 0, 0, 0  # 对应因数2, 3, 5的指针
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1

        return dp[n - 1]
