from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 滑动窗口法
        # 定义双指针, 左闭右闭
        if target <= 2:
            return []
        i = 1   # 左指针从1开始
        j = 1   # 右指针从1开始
        sum = 1 # 窗口和
        res = []
        while i <= target // 2: # 左指针不会大于target的一半
            if sum < target:    # 窗口和小于目标值
                # 右指针先右移, 再更新窗口和
                j += 1
                sum += j
            elif sum > target:  # 窗口和大于目标值
                # 先更新目标和, 再将左指针右移
                sum -= i
                i += 1
            else:   # sum == target, 找到一组连续正整数
                res.append(list(range(i, j+1)))
                # 更新窗口和, 整个窗口右移1格, 注意顺序
                sum -= i
                i += 1
                j += 1
                sum += j

        return res
