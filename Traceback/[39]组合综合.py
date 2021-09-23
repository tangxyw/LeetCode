from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 深度优先遍历+回溯+剪枝
        self.res = []
        track = []

        def traceback(s: int, track: List[int]):
            if s == target:  # 得到一个合法结果
                self.res.append(track[:])
                return
            if s > target:  # 当前数字和已经大于目标, 剪枝
                return

            for num in candidates:  # 遍历候选列表
                if not track or num >= track[-1]:  # 为避免重复, 保证track是单调不减序列
                    track.append(num)
                    traceback(s + num, track)  # 向下递归
                    track.pop()  # 回溯

        traceback(0, track)
        return self.res
