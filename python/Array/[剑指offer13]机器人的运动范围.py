class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 深度优先遍历
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        def isValid(x: int, y: int) -> bool:
            """判断x, y的位数和是否大于k"""
            s = 0
            while x > 0:
                s += x % 10
                x = x // 10
            while y > 0:
                s += y % 10
                y = y // 10
            return s <= k

        # 定义递归函数
        def dfs(x: int, y: int):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1:  # 索引越界
                return 0
            if not isValid(x, y):  # 索引位数和大于k
                return 0
            if matrix[x][y] == 1:  # 已经计算过
                return 0
            matrix[x][y] = 1  # 标记为已探索
            # 向四个方向递归
            return dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1) + 1
        # 从(0, 0)开始
        return dfs(0, 0)
