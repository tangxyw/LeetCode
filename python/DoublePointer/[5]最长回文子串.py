class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩散法
        res = ""  # 最大回文串

        for i in range(len(s)):  # 遍历s中的每个字符char
            left = i - 1  # char左边字符的index
            right = i + 1  # char右边字符的index
            # 先向左
            while left >= 0 and s[i] == s[left]:
                left -= 1  # left指针停在左侧第一个不等于s[i]的位置上
            # 再向右
            while right < len(s) and s[i] == s[right]:
                right += 1  # right指针停在左侧第一个不等于s[i]的位置上
            # 再向两侧一起扩散
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # 左右指针停在左右两侧第一个不相等的位置上
                right += 1
            if right - left - 1 > len(res):  # 更新最大回文串
                res = s[left+1:right]
        return res
