import math
from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        # 厄拉多塞筛法
        nums_type = [True] * n  # 标识1-n每个数字是否为素数
        for i in range(2, int(math.sqrt(n)) + 1):  # 由于因式分解的对称性, 只遍历到sqrn(n)就可以了
            if nums_type[i]:  # 索引i的值为True
                for j in range(i * i, n, i):  # i*i之前的已经遍历完了, 从i*i开始遍历, step为i (相当于遍历i*(i+1),i*(i+2)...)
                    nums_type[j] = False  # 这些都是合数

        count = 0
        # 素数计数
        for i in range(2, n):
            if nums_type[i]:
                count += 1

        return count
