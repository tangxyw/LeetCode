from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        # 从第2个字符串开始遍历
        for i in range(1, len(strs)):
            j = 0
            # 遍历字符串中每一个字符, 遍历长度为当前res和当前字符串中较短的
            while j < min(len(res), len(strs[i])) and res[j] == strs[i][j]:
                # 逐字符相比, 直到找到不一样的
                j += 1
            # 每遍历一个字符串, 就更新res
            res = res[:j]

        return res
