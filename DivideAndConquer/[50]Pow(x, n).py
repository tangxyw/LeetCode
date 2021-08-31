class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 分治法
        # base case
        if n == 0:
            return 1.0

        if n < 0:  # 把n<0的情况统一到n>=0
            return 1 / self.myPow(x, -n)
        else:
            y = self.myPow(x, n // 2)
            if n % 2 == 1:  # n为奇数
                return y * y * x
            else:
                return y * y