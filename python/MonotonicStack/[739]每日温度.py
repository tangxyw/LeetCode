from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # 单调栈, 存放温度index, 从栈底到栈顶递减

        for i in range(n):
            # 只要stack不为空 且 当前温度高于栈顶温度, 就能更新栈顶索引的下一个高温值
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            # stack为空 或 当前温度不高于栈顶温度, 将当前温度索引压入栈
            stack.append(i)

        # 最后stack中的元素, 都是没有下一个高温的, 默认为0, 无需处理
        return res
