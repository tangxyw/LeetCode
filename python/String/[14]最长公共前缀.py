from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:  # 只有一个字符串要特殊处理
            return strs[0]

        flag = 0  # 循环结束标识
        res = []
        i = 0  # 当前比较字符的索引
        while True:
            for j in range(len(strs)):  # 遍历所有字符串
                if j == 0:  # 第1个字符串的第i个字符选为标准
                    pre = strs[j][i:i + 1]  # 取切片即使越界不会报错
                else:  # 从第2个字符串开始
                    if strs[j][i:i + 1] != pre or not pre:  # 与标准不一致或者标准为空
                        flag = 1  # 给外层循环传递信号
                        break  # 结束循环
            if flag == 1:  # 监测信号
                break
            res.append(pre)
            i += 1

        return "".join(res)