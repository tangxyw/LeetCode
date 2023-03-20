from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)  # 去重

        for num in nums_set:
            if num - 1 not in nums_set:  # 只遍历那些自身-1不在集合中的数字(作为连续序列起点)
                cur_num = num
                cur_length = 1
                while cur_num + 1 in nums_set:  # 从当前数字一直往后数, 直到不在集合中
                    cur_num += 1
                    cur_length += 1
                longest = max(longest, cur_length)  # 更新最长序列长度

        return longest
