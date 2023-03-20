class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 双指针
        # p指向s, q指向t
        p, q = 0, 0
        while p < len(s) and q < len(t):  # 依次比较s和t的每一个字符
            if s[p] == t[q]:  # p和q位置的字符相等
                p += 1  # s的指针p向前移动一格
            q += 1  # 每次迭代t的指针q都向前移动一格
        # 遍历结束后, 只有s的指针走到最后, s才为t的一个子序列
        return p == len(s)
