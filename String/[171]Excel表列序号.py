class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 26进制转10进制
        sum = 0
        multiple = 1
        for i in range(1, len(columnTitle) + 1):  # 从后向前遍历字符串
            sum += (ord(columnTitle[-i]) - ord("A") + 1) * multiple  # 当前位字母与A的距离*乘子
            multiple *= 26  # 更新下一位的乘子

        return sum
