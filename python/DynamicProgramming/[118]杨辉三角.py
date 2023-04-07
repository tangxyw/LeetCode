from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):    # 迭代杨辉三角的行
            layer_res = []  # 存放每行数字
            for j in range(i + 1):  # 迭代每行的数字, 当前行长度为i+1
                if j == 0 or j == i:    # 两端的数字都为1
                    layer_res.append(1)
                else:   # 注意迭代到i=2时才会涉及这里
                    layer_res.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(layer_res)

        return res
