from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):  # 从各位开始遍历
            digits[i] += 1  # 当前位数字+1
            if digits[i] == 10: # 需要进位
                digits[i] = 0
            else:   # 不需要进位了, 返回结果
                return digits

        # 处理所有数字全为9的特例, 首位补1
        digits = [1] + digits
        return digits