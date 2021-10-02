from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯+剪枝
        nums = list(range(1, n+1))  # 自动升序排列
        self.res = []
        track = []

        def traceback(nums, track):
            if len(track) == k:
                self.res.append(track[:])
                return
            if len(track) + len(nums) < k:  # 剪枝
                return

            for i, num in enumerate(nums):
                track.append(num)
                traceback(nums[i+1:], track)
                track.pop()

        traceback(nums, track)
        return self.res
