from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # dfs+回溯+剪枝
        n = len(nums)
        nums.sort()  # 预先升序排序
        track = []
        res = []

        def traceback(nums, track):
            if len(track) == n:  # 到底了, 返回结果
                res.append(track[:])
                return

            for i in range(len(nums)):
                if i == 0 or (i > 0 and nums[i] > nums[i - 1]):  # 重复值连续, 只取第一个, 后面的被剪枝
                    track.append(nums[i])
                    traceback(nums[:i] + nums[i + 1:], track)  # 扣掉nums[i], 向下递归
                    track.pop()  # 回溯

        traceback(nums, track)
        return res