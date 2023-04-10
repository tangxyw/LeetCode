from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 深度优先遍历+备忘录剪枝
        self.global_res = False  # 最终结果
        memo = set()  # 备忘录, 存放无法进行拆分的子串start索引
        n = len(s)

        def dfs(start: int) -> bool:
            if self.global_res:
                return True
            if start == n:  # 可以拆分
                self.global_res = True
                return True
            if start in memo:  # 查找备忘录，如果找到, 剪枝
                return False

            inner_res = False
            for i in range(start, n + 1):  # 从start开始遍历子串的前i个字符
                if s[start:i] in wordDict:
                    inner_res = dfs(i) or inner_res  # 更新本次递归结果
            if not inner_res:  # 本次递归结果为False, 就将start加入到memo中
                memo.add(start)
                return False

        dfs(0)
        return self.global_res
