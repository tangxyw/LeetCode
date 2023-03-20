from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        max_num = pow(10, n)
        return list(range(1, max_num))
