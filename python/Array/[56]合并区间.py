from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先按区间左端点升序排序, 使得可以合并的区间连续
        intervals.sort(key=lambda x: x[0])

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:  # res为空 or res的最后一个区间的右端点<当前区间左端点
                res.append(interval)
            else:  # res的最后一个区间的右端点>=当前区间左端点
                res[-1][1] = max(res[-1][1], interval[1])  # 更新res最后一个区间的右端点

        return res
