class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []  # 存放最终结果
        track = []  # 存放遍历过程中的每一个排列, 注意这是一个全局变量

        def traceback(nums: List[int], track):
            # 深度优先遍历+回溯
            if len(track) == len(nums):  # 排列的长度和nums一样, 说明已经得到一个排列
                self.res.append(track[
                                :])  # 将得到的排列加到结果集中, 注意track是一个指针, track改变res也跟着改, 所以这时应该把当时track的一个快照拷贝下来再加到res中, 否则最后回溯到根节点时track为[]

            for num in nums:  # 在每一层递归中遍历候选列表
                if num in track:  # 若该数字已经在排列中, 迭代下一个数字
                    continue
                track.append(num)  # 否则将该数字加到排列中
                traceback(nums, track)  # 今日下一层递归
                track.pop()  # 因为track是全局变量, 所以递归完后要回溯, 保证track的准确性

        traceback(nums, track)
        return self.res
