from typing import List

class Solution:

    # 方法一
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        # 全部子集问题就是遍历每一个元素, 选择是否把该元素放到集合里, 找到所有可能, 实际是遍历层数为nums长度的满二叉树问题
        res = []
        track = []
        n = len(nums)

        def traceback(index, trace):
            if index == n:
                res.append(track[:])
                return

            # 选择当前index的值, 需要回溯
            trace.append(nums[index])
            traceback(index + 1, trace)
            trace.pop()

            # 不选择, 不需要回溯
            traceback(index + 1, trace)

        traceback(0, track)
        return res

    # 方法二
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        # 与方法一不同，方法二在所有节点给出结果
        # 方法二比方法一效率高
        res = []
        track = []
        n = len(nums)

        def traceback(index, trace):
            # 从根节点开始, 每个中间节点都是结果
            res.append(track[:])
            if index == n:
                return

            for i in range(index, n):
                trace.append(nums[i])
                traceback(i + 1, trace)
                trace.pop()

        traceback(0, track)
        return res

