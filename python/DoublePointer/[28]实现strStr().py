class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 暴力方法
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(haystack) < len(needle):
            return -1

        # 左右指针之间的长度为len(needle), 左闭右开
        left = 0
        right = len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            # 左右指针同时向右移动
            left += 1
            right += 1
        return -1
