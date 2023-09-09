from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 单一元素左边的所有成对元素, 索引组合都为"偶奇"
        # 单一元素右边的所有成对元素, 索引组合都为"奇偶"

        n = len(nums)
        left, right = 0, n - 1

        # 数组两端扩展
        def get(index):
            if index < 0:
                return float('-inf')
            if index >= n:
                return float('inf')
            return nums[index]

        while left <= right:
            mid = left + (right - left) // 2
            if get(mid - 1) < get(mid) < get(mid + 1):  # 满足单一元素的条件
                return nums[mid]
            if get(mid) == get(mid - 1):    # mid元素和ta左边相等
                if mid % 2 == 0:  # 且mid为偶数时
                    right = mid - 2
                else:   # mid为奇数时
                    left = mid + 1
            else:
                if mid % 2 == 0:  # m且mid为偶数时
                    left = mid + 2
                else:   # mid为奇数时
                    right = mid - 1
