from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 结果矩阵
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        # 初始上下左右的边界
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        # 从1开始填充
        j = 1

        while j <= n * n:  # 一共填充n*n个数字
            # 左到右
            for i in range(left, right + 1):
                if j <= n * n:
                    matrix[top][i] = j
                    j += 1
            top += 1  # 上边界下移

            # 上到下
            for i in range(top, bottom + 1):
                if j <= n * n:
                    matrix[i][right] = j
                    j += 1
            right -= 1  # 右边界左移

            # 右到左
            for i in range(right, left - 1, -1):
                if j <= n * n:
                    matrix[bottom][i] = j
                    j += 1
            bottom -= 1  # 下边界上移

            # 下到上
            for i in range(bottom, top - 1, -1):
                if j <= n * n:
                    matrix[i][left] = j
                    j += 1
            left += 1  # 左边界右移

        return matrix
