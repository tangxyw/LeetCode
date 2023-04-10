from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        track = []
        n = len(s)

        def traceback(index: int, track: List[str]):
            # index为当前递归起始字符索引
            if index == n:  # 遍历完最后一个字符
                self.res.append(track[:])
                return

            for i in range(index, n):  # 遍历每一种分割方法
                if issymmetry(index, i):  # 只考虑回文串, 其他情况剪枝
                    track.append(s[index:i + 1])
                    traceback(i + 1, track)  # 向后一个字符递归
                    track.pop()  # 回溯

        def issymmetry(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        traceback(0, track)
        return self.res
