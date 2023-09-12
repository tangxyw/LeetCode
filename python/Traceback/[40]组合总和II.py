from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        track = []
        res = []

        def traceback(start: int, track: List[int], target: int) -> None:
            if target == 0:
                res.append(track[:])
                return

            for i in range(start, n):
                if i > start and candidates[i - 1] == candidates[i]:    # 剪枝
                    continue
                if candidates[i] <= target:
                    track.append(candidates[i])
                    traceback(i + 1, track, target - candidates[i])
                    track.pop()

        traceback(0, track, target)

        return res

