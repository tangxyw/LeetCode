from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 深度优先遍历
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):  # 索引越界
                return
            if grid[i][j] == "0":  # 当前格子不为岛屿, 探索完毕返回
                return
            grid[i][j] = "0"  # 将当前格子置为0, 以免陷入无限循环
            # 向上下左右四个方向递归
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":  # 找到岛屿的一部分(边界)
                    res += 1  # 岛屿数量+1
                    dfs(i, j)

        return res
