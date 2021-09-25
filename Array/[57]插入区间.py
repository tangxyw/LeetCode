from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        left, right = newInterval  # 待插入区间左右端点
        res = []
        i = 0

        # 第一阶段, newInterval左边不与之相交的区间, 直接插入res
        while i < n and intervals[i][1] < left:
            res.append(intervals[i])
            i += 1

        # 第二阶段, 每一个与newInterval相交的区间都与至合并成新的newInterval, 即更新left和right
        while i < n and intervals[i][0] <= right:
            left = min(intervals[i][0], left)
            right = max(intervals[i][1], right)
            i += 1
        res.append([left, right])

        # 第三阶段, newInterval右边不与之相交的区间, 直接插入res
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
