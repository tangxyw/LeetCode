from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        track = []

        # 深度优先遍历+剪枝+回溯
        def traceback(s, track):
            if len(s) == 0:  # s为空字符串, 已经分割完毕,到达最底层
                self.res.append(track[:])  # 注意是track的拷贝
                return
            for i in range(1, len(s) + 1):  # 遍历每一种分割方法
                if isSymmetry(s[:i]):  # 判断前缀字符串s[:i]是一个回文字符串, 如果不是就剪枝
                    track.append(s[:i])  # 将s[:i]加入track
                    traceback(s[i:], track)  # 向下一层递归, 字符串变为余下的后缀字符串
                    track.pop()  # 回溯

        def isSymmetry(s: str) -> bool:
            left, right = 0, len(s) - 1
            while (left < right):
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        traceback(s, track)
        return self.res