from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        memo = {}

        def dfs(x: int, y: int, last_val: int) -> int:
            if x < 0 or x >= m or y < 0 or y >= n:  # 非法坐标
                return 0

            cur_val = matrix[x][y]
            if cur_val <= last_val:  # 路径是递增的
                return 0

            # 向四个方向递归, 注意要+1
            if (x, y) in memo:  # 如果在备忘录里能找到, 就可以直接返回
                return memo[(x, y)]

            dfs_res = max(dfs(x - 1, y, cur_val),
                          dfs(x + 1, y, cur_val),
                          dfs(x, y - 1, cur_val),
                          dfs(x, y + 1, cur_val)) + 1

            memo[(x, y)] = dfs_res  # 本次递归结果记录在备忘录中

            return dfs_res

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, float('-inf')))

        return res



