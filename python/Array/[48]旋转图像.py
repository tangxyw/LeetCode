from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 将matrix[i][j]的元素放到matrix[j][n-i-1]上, n = len(matrix)
        # 两步走:
        # step1: 将matrix[i][j]和matrix[n-i-1][j]交换
        # step2: 将matrix[i][j]和matrix[j][i]交换

        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]