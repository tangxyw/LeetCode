class Solution:
    def trailingZeroes(self, n: int) -> int:
        # https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/172-jie-cheng-hou-de-ling-by-chi2nagisa-6yc9/
        count = 0
        while n > 0:
            count += n // 5
            n = n // 5

        return count
