from typing import List
import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # https://leetcode-cn.com/problems/largest-number/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-vn86e/
        strs = map(str, nums)

        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1

        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'  # 特殊case: nums元素为多个0
