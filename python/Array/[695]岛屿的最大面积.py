from typing import  List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0    # 最大面积

        def dfs(x: int, y: int) -> int:
            # 深度优先遍历
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0

            if grid[x][y] == 0:
                return 0

            grid[x][y] = 0  # 当前坐标为1, 置为0
            return dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1) + 1    # 向四个方向递归, 注意+1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area = dfs(i, j)
                    max_area = max(max_area, cur_area)

        return max_area


