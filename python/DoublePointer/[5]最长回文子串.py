class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩散法
        max_len = 0 # 最大回文串长度
        max_start = 0   # 最大回文串起始index
        for i in range(len(s)): # 遍历s中的每个字符char
            left = i - 1    # char左边字符的index
            right = i + 1   # char右边字符的index
            length = 1  # 当前回文字符串长度
            # 先向左
            while(left >= 0 and s[i] == s[left]):
                left -= 1   # left指针停在左侧第一个不等于s[i]的位置上
                length += 1
            # 再向右
            while(right < len(s) and s[i] == s[right]):
                right += 1  # right指针停在左侧第一个不等于s[i]的位置上
                length += 1
            # 再向两侧一起扩散
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1   # 左右指针停在左右两侧第一个不相等的位置上
                right += 1
                length += 2
            if length > max_len:    # 更新最大回文串的长度和起始位置
                max_len = length
                max_start = left + 1    # 注意这里要+1
        return s[max_start: max_start+max_len]