from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = []
        track = []

        # 深度优先遍历+剪枝+回溯
        def traceback(s, track):
            if len(s) == 0:  # s为空字符串, 已经分割完毕,到达最底层
                self.res.append(' '.join(track))  # 把track拼成句子
            for i in range(1, len(s) + 1):  # 遍历每一种分割方法
                if s[:i] in wordDict:  # 判断前缀字符串s[:i]是否在字典里, 如果不在就剪枝
                    track.append(s[:i])
                    traceback(s[i:], track)  # 向下一层递归, 字符串变为余下的后缀字符串
                    track.pop()  # 回溯

        traceback(s, track)
        return self.res
