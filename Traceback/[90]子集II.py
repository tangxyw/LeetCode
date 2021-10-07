from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # dfs+回溯+剪枝
        # 与[78]子集的递归方式不同, 本题的递归树中, 每个节点都是一个结果, 第i层的所有节点代表元素个数为i的子集
        # https://leetcode-cn.com/problems/subsets-ii/solution/90-zi-ji-iiche-di-li-jie-zi-ji-wen-ti-ru-djmf/
        nums.sort()  # 先排序
        n = len(nums)
        self.res = []
        track = []

        def traceback(nums, track):
            # 每个节点都是一个子集
            self.res.append(track[:])

            for i, num in enumerate(nums):
                # 除第一个出现的数字外, 后面的重复数字被剪枝
                if i == 0 or nums[i] != nums[i - 1]:
                    track.append(num)
                    traceback(nums[i + 1:], track)
                    track.pop()

        traceback(nums, track)
        return self.res
