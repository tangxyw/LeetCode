from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列, 使用双向队列实现
        # 一共有n-k+1个窗口
        res = []
        q = deque()  # 存放索引, 索引是单调递增的, 索引对应的值是单调递减的, 每迭代1个窗口, 都返回q[0]为窗口内最大元素
        for i in range(k):  # 首先处理前k个元素, 即第1个窗口
            while q and nums[i] >= nums[q[-1]]:  # q非空且当前值>=队列末尾元素
                q.pop()  # 弹出队列末尾元素
            q.append(i)  # 将当前索引加入队列
        res.append(nums[q[0]])

        for i in range(k, len(nums)):  # 从第2个窗口开始遍历, i为窗口最后一个元素的索引
            while q and nums[i] >= nums[q[-1]]:  # q非空且当前值>=队列末尾元素
                q.pop()  # 弹出队列末尾元素
            q.append(i)  # 将当前索引加入队列
            while q[0] <= i - k:  # 若q[0]已经不在当前窗口, 则从q左侧弹出
                q.popleft()
            res.append(nums[q[0]])  # 这时的q[0]已经在当前窗口内, 且是窗口最大值

        return res