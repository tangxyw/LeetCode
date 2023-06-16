from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 预先排序
        n = len(nums)
        res = []
        visited = [False] * n  # 记录每个num是否在track里
        track = []

        def traceback(depth: int, track: List[int]) -> None:
            if depth == n:  # 深度到n的时候正好为一个排列
                res.append(track[:])
                return

            for i in range(n):
                # 剪枝条件
                # 1. 当前位置的数字已经在track里
                # or
                # 2. 当前数字与前一个数字一样, 且前一个数字没有在track里(在递归树的每一层, 相同数字只使用没用过的第一个)
                if visited[i] or (i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]):
                    continue
                visited[i] = True  # 已使用标记
                track.append(nums[i])
                traceback(depth + 1, track)  # 向下递归
                track.pop()  # 回溯
                visited[i] = False  # 标记回溯

        traceback(0, track)

        return res
