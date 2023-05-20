from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # bfs, 模拟层序遍历
        n = len(nums)
        step = 0  # 最终结果
        right = 0  # 上一次跳跃到的最右侧边界
        max_far = 0  # 当前能跳到的最远位置

        for i in range(n - 1):  # 无需遍历最后一个元素
            max_far = max(max_far, nums[i] + i)  # 计算最远位置
            if i == right:  # 到了最右侧边界, 相当于层次遍历遍历完了当前层
                right = max_far  # 更新最右侧边界
                step += 1  # 跳跃次数+1
                if right >= n - 1:  # 右边界越界
                    return step  # 返回当前步数

        # 特殊case: [0]
        return step
