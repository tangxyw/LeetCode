from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # https://leetcode.cn/problems/house-robber-ii/solution/213-da-jia-jie-she-iidong-tai-gui-hua-jie-gou-hua-/
        def myrob(start: int, end: int) -> int:
            pre = 0
            cur = nums[start]

            for i in range(start + 1, end + 1):
                pre, cur = cur, max(cur, pre + nums[i])

            return cur

        if len(nums) == 1:
            return nums[0]

        return max(myrob(1, len(nums) - 1), myrob(0, len(nums) - 2))
