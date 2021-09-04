from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或运算
        # https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
        res = 0
        for num in nums:
            res ^= num
        return res
