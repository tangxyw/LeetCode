from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列, 使用双向队列实现
        # 一共有n-k+1个窗口
        res = []
        q = deque()  # 存放索引, 索引是单调递增的, 索引对应的值是单调递减的, 每迭代1个窗口, 都返回q[0]为窗口内最大元素
        for i in range(len(nums)):  # i为窗口的右端点
            while q and nums[i] >= nums[q[-1]]:  # q非空且当前值>=队列末尾元素
                q.pop()  # 弹出队列末尾元素
            q.append(i)  # 将当前索引加入队列

            while q[0] <= i - k:  # q[0]不在当前窗口
                q.popleft()  # 弹出

            if i >= k - 1:  # i为k-1时才是第一个窗口
                res.append(nums[q[0]])

        return res
