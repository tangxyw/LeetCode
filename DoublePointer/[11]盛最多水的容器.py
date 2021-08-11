from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # https://leetcode-cn.com/problems/container-with-most-water/solution/on-shuang-zhi-zhen-jie-fa-li-jie-zheng-que-xing-tu/
        # 双指针
        left = 0
        right = len(height) - 1

        maximum = 0
        while left < right:
            s = min(height[left], height[right]) * (right - left)   # 计算盛水量
            maximum = max(maximum, s)   # 更新最大值
            # 比较左右边界, 哪个边界高度低, 哪边向内侧收缩1步, 该方法的正确性证明见注释中的链接
            if height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1

        return maximum
