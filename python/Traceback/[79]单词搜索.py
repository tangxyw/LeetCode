from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y, index):
            """
                x, y: board中的坐标
                index: word的索引, 当前dfs寻找的目标

                return: 能找到返回True, 否则为False
            """
            # 当前坐标不是要找的字符
            if board[x][y] != word[index]:
                return False
            # 找到目标单词路径
            if index == len(word) - 1:
                return True

            # 当前位置字符标为已使用, 避免递归时再次搜索到
            used[x][y] = True
            # 向四个方向递归
            for delta_x, delta_y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + delta_x, y + delta_y
                # 坐标合法 and 当前位置字符之前未被使用 and 下层递归结果为真
                # 这里用到了截断判断的技巧, 使得非法的坐标不会作为dfs的参数
                if 0 <= nx < m and 0 <= ny < n and not used[nx][ny] and dfs(nx, ny, index + 1):
                    return True
            # 一定记住回溯
            used[x][y] = False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


