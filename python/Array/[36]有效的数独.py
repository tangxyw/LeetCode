from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]  # 记录每一行的数字计数
        col = [{} for _ in range(9)]  # 记录每一列的数字计数
        box = [{} for _ in range(9)]  # 记录每一个3x3区域的数字计数, 从左到右从上到下依次编号0-8

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':  # 遇到数字
                    num = int(num)
                    # 在相应的地方做计数
                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    box_index = (i // 3) * 3 + j // 3  # 产生与box一致的序号
                    box[box_index][num] = box[box_index].get(num, 0) + 1

                    if row[i][num] > 1 or col[j][num] > 1 or box[box_index][num] > 1:
                        return False

        return True