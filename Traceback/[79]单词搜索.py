from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 深度优先遍历+剪枝
        def dfs(pre_word_coords, index, track):
            """
                pre_word_coords: 路径中前面字母的坐标集合
                index: 需要寻找的letter在word中的索引
                track: 当前路径
            """
            if len(track) == len(word):
                self.res = True
                return

            if not pre_word_coords:  # 第一个letter
                coordinates = findLetterXY(board, word[index])
            else:  # 在pre_word_x, pre_word_y上下左右范围内找下一个letter的坐标
                coordinates = findNextLetter(board, pre_word_coords, word[index])

            if not coordinates:  # 没有候选集, 剪枝
                return

            for coord in coordinates:
                track.append(word[index])
                dfs(pre_word_coords + [coord], index + 1, track)  # 向下一个letter递归
                track.pop()  # 回溯

        def findLetterXY(board: List[List[str]], letter: str):
            """在board中寻找letter, 返回letter的坐标(可能多个, 可能为空)"""
            res = []
            for i, line in enumerate(board):
                for j, s in enumerate(line):
                    if s == letter:
                        res.append((i, j))
            return res

        def findNextLetter(board: List[List[str]], pre_word_coords: List, letter: str):
            """在board中的pre_word_coords[-1]周围寻找letter, 返回letter的合法坐标(可能多个, 可能为空), 合法坐标表示坐标不能越界, 也不能是路径中前面字母的坐标"""
            res = []
            last_coords_x, last_coords_y = pre_word_coords[-1]
            x_max = len(board) - 1
            y_max = len(board[0]) - 1
            if last_coords_x + 1 <= x_max and board[last_coords_x + 1][last_coords_y] == letter and (
                    last_coords_x + 1, last_coords_y) not in pre_word_coords[:-1]:
                res.append((last_coords_x + 1, last_coords_y))
            if last_coords_x - 1 >= 0 and board[last_coords_x - 1][last_coords_y] == letter and (
                    last_coords_x - 1, last_coords_y) not in pre_word_coords[:-1]:
                res.append((last_coords_x - 1, last_coords_y))
            if last_coords_y + 1 <= y_max and board[last_coords_x][last_coords_y + 1] == letter and (
                    last_coords_x, last_coords_y + 1) not in pre_word_coords[:-1]:
                res.append((last_coords_x, last_coords_y + 1))
            if last_coords_y - 1 >= 0 and board[last_coords_x][last_coords_y - 1] == letter and (
                    last_coords_x, last_coords_y - 1) not in pre_word_coords[:-1]:
                res.append((last_coords_x, last_coords_y - 1))
            return res

        self.res = False
        dfs([], 0, [])
        return self.res
