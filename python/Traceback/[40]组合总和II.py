from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
        # 深度优先遍历+回溯+剪枝
        self.res = []
        track = []
        candidates.sort()  # 将candidates升序排列, 避免重复

        def traceback(s: int, start: int, track: List[int]):
            # start为candidates索引
            if s == target:
                self.res.append(track[:])
                return
            if s > target:
                return

            for i in range(start, len(candidates)):  # 从start开始遍历
                if i == start or candidates[i] > candidates[i - 1]:  # 如果有重复数值, 则只对第一个出现的进行递归, 其他的被剪枝
                    track.append(candidates[i])  # 将符合条件的数值放进track
                    traceback(s + candidates[i], i + 1, track)  # 更新s和start, 向下递归
                    track.pop()  # 回溯

        traceback(0, 0, track)
        return self.res
