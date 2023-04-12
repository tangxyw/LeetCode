from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        # https://leetcode.cn/problems/majority-element/solution/3chong-fang-fa-by-gfu-2/
        counter = 0  # 计数器
        cur_num = nums[0]  # 当前数字

        for num in nums:
            if cur_num == num:  # num与当前数字一致, counter增加1
                counter += 1
            elif counter == 0:  # num与当前数字不一致, 且counter为0, num成为新的当前数字
                cur_num = num
            else:  # num与当前数字不一致, 且counter>0, counter减少1
                counter -= 1

        return cur_num
