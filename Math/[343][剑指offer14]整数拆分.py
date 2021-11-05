import math


class Solution:
    def integerBreak(self, n: int) -> int:
        # https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/
        # 特殊case
        if n <= 3:
            return n - 1
        # d为n除以3的商, m为余数
        d = n // 3
        m = n % 3
        if m == 0:  # 余数为0, 结果为3的d次幂
            return int(math.pow(3, d))
        if m == 1:  # 余数为1, 要把一个3拆成1和2, 其中1要和余数1再组成2
            return int(math.pow(3, d - 1) * 4)
        if m == 2:  # 余数为2, 直接在3的d次幂后再乘2
            return int(math.pow(3, d) * 2)
