from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1)方法
        row = len(matrix)
        col = len(matrix[0])

        row_flag = col_flag = False

        # 检查第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col_flag = True
                break

        # 检查第一行是都有0
        for j in range(col):
            if matrix[0][j] == 0:
                row_flag = True
                break

        # 把第一行和第一列看做标志位, 该行或该列有0, 则把相第一行或第一列对应的位置置为0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # 根据标志位置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 若原始matrix第一行有0, 则把第一行都置为0
        if row_flag:
            for j in range(col):
                matrix[0][j] = 0

        # 若原始matrix第一列有0, 则把第一列都置为0
        if col_flag:
            for i in range(row):
                matrix[i][0] = 0
