class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        left, right = 0, 0
        res = 0
        window_set = dict()  # 窗口内的字符和出现次数

        while right < len(s):  # 迭代结束条件是右指针到达字符串尾部
            # 窗口右端点右移, 窗口扩大
            c = s[right]  # 当前右端点字符
            window_set[c] = window_set.get(c, 0) + 1  # 窗口更新, 右端点+1
            while window_set[c] > 1:  # 右端点为当前窗口内重复字符, 移动左端点直到没有重复(也就是把左端点移动到前面重复字符的后面)
                # 窗口左端点右移, 窗口缩小
                d = s[left]  # 左端点字符
                window_set[d] -= 1  # 窗口更新, 左端点-1
                left += 1  # 左端点右移
            right += 1  # 右端点右移
            res = max(res, right - left)  # 更新最大无重复子串长度

        return res
