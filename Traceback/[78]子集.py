from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.set = [True, False]    # 全部子集问题就是遍历每一个元素, 选择是否把该元素放到集合里, 找到所有可能, 实际也是树遍历问题
        self.res = []
        track = []  # 存放每一个子集, 也就是路径

        def traceback(nums, track):
            if not nums:    # 到达叶节点了
                self.res.append(track[:])   # 注意append的必须是track的一个拷贝
            else:
                for flag in self.set:   # 选择是否将元素放入路径
                    if flag:    # 如果是True就放入, 是False就什么都不做
                        track.append(nums[0])
                    traceback(nums[1:], track)  # 向下一个元素递归
                    if flag:    # 如果本层将元素放入了路径, 那么就需要回溯, 没放入就不需要
                        track.pop()

        traceback(nums, track)
        return self.res