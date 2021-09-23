from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分查找
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        # 上述遍历没有找到target
        # 分两种情况讨论
        # 1.
        # 在最后一次遍历中, 有left = right = mid, 即nums中只剩1个数值, 令其为x
        # 当x < target时, left右移一位, 此时left就为target插入的位置
        # 当x > target时, left不变, left也为target插入位置
        # 2.
        # 在最后一次或倒数第二次遍历中, 有left = right - 1, mid = left, 即nums中剩2个数值, nums[mid]为靠左的数值, 令其为x
        # 当x < target时, left右移一位, 此时left = right, 进入下一次迭代, 最终属于情况1
        # 当x > target时, left不变, right = mid - 1 = left - 1, 不满足while条件结束遍历, 这是left为插入位置
        return left
