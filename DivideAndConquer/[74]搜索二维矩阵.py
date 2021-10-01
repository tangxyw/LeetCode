from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 两次二分查找
        top = 0
        bottom = len(matrix) - 1

        # 第一次二分查找, 寻找target所在行
        while top <= bottom:  # 注意这里一定要有=
            mid = top + (bottom - top) // 2  # 若区间元素个数为偶数, 则mid指向中间靠左的那个
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
        # 遍历完成后, top应该在bottom的下边

        # 行索引为上面迭代后的bottom值
        row = bottom
        # 所有行的第一个元素都不是target
        left = 1
        right = len(matrix[0]) - 1

        # 第二次二分查找, 在row中寻找target
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
        # 没找到
        return False
