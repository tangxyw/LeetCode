class Solution:
    def firstUniqChar(self, s: str) -> str:
        # https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
        d = {}
        # 遍历字符串s
        for char in s:
            # 若char没在d中(即第1次出现), 则置为True, 反之(第N次出现)置为False
            d[char] = not char in d
        for k, v in d.items():  # 取字典中第1个不为False的key(python3.6之后字典的key的顺序为添加顺序)
            if v:
                return k
        return ' '
