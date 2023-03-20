class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        start, end = 0, n - 1  # 最后一个单词起始和末尾索引
        for i in range(n - 1, -1, -1):  # 从字符串最后开始遍历, 找到第一个不是空格的索引, 为end
            if s[i] != " ":
                end = i
                break

        for j in range(end - 1, -1, -1):  # 再从end开始向前遍历, 找到第一个是空格的索引, 右移一位为start
            if s[j] == " ":
                start = j + 1
                break

        # 返回单词长度
        return end - start + 1
