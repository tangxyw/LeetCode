from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针
        # https://zhuanlan.zhihu.com/p/107792266?hmsr=toutiao.io
        # 一个位置的雨水量, 等于min(所有左边柱子的最大高度, 所有右边柱子的最大高度) - 该位置柱子高度
        n = len(height)
        res = 0

        left = 0
        right = n - 1

        l_max = height[left]  # 存放0到left(都是闭区间)的最大值
        r_max = height[right]  # 存放right到n-1(都是闭区间)的最大值

        while left <= right:  # 遍历height
            l_max = max(l_max, height[left])  # 更新l_max
            r_max = max(r_max, height[right])  # 更新r_max
            if l_max < r_max:  # 蕴涵当前位置左边的最大值比右边的最大值小, 具体解释可见注释链接
                res += l_max - height[left]  # 这时计算的是当前left索引的雨水量
                left += 1  # 进入下一轮迭代
            else:  # 同上
                res += r_max - height[right]
                right -= 1

        return res
