from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 类似二分搜索
        # 左下角的数值, 与它同行的数值都比它大, 与它同列的数值都比它小
        # 每次比较左下角与target, 根据结果进行剪枝

        m = len(matrix)  # 行数
        n = len(matrix[0])  # 列数

        # 左下角坐标初值
        row = m - 1
        col = 0

        while row >= 0 and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:  # 左下角比target大, 剪枝当前行
                row -= 1
            elif matrix[row][col] < target:  # 左下角比target小, 剪枝当前列
                col += 1

        return False