from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        self.res = []
        track = []
        # 记录每个元素是否已经使用
        used = [False] * len(s)
        # 字符排序
        s_list = [c for c in s]
        s_list.sort()

        def traceback(i, track):
            # i为递归深度, 也是track内字符的个数
            if i == len(s):
                self.res.append("".join(track))
                return

            # 遍历s的每一个字符
            for j in range(len(s)):
                """
                当下面条件同时满足时, 才进行向下递归:
                1. 当前字符之前没有使用过
                2. s的第一个字符 or 当前字符和前一个字符不同 or 前一个字符没有使用过
                解释最后一个条件: 当前字符和前一个字符相同, 且不是第一个字符时, 若前一个字符已经使用过了, 那么当前字符也要加入track并递归, 否则会遗漏.
，               """
                if not used[j] and (j == 0 or s_list[j] != s_list[j - 1] or used[j - 1]):
                    used[j] = True
                    track.append(s_list[j])
                    traceback(i + 1, track)
                    # 回溯需要2个操作
                    track.pop()
                    used[j] = False

        traceback(0, track)
        return self.res
