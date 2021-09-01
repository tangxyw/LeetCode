from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        # 初始上下左右的边界
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        # 剩余未返回的元素个数
        restNums = len(matrix) * len(matrix[0])
        # 最终结果
        res = []

        while restNums >= 1:  # 直到所有元素都被遍历完
            # 左到右
            for i in range(left, right + 1):
                if restNums >= 1:
                    res.append(matrix[top][i])
                    restNums -= 1
            top += 1  # 上边界下移

            # 上到下
            for i in range(top, bottom + 1):
                if restNums >= 1:
                    res.append(matrix[i][right])
                    restNums -= 1
            right -= 1  # 右边界左移

            # 右到左
            for i in range(right, left - 1, -1):
                if restNums >= 1:
                    res.append(matrix[bottom][i])
                    restNums -= 1
            bottom -= 1  # 下边界上移

            # 下到上
            for i in range(bottom, top - 1, -1):
                if restNums >= 1:
                    res.append(matrix[i][left])
                    restNums -= 1
            left += 1  # 左边界右移

        return res
