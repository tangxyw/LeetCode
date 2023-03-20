from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 转化为寻找环形链表的环起点
        # 参考[142]环形链表II
        # https://leetcode-cn.com/problems/find-the-duplicate-number/solution/287xun-zhao-zhong-fu-shu-by-kirsche/

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
