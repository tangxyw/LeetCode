from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 分治法, 本质其实是后序遍历递归
        # base case: 只有一个元素时, 返回该元素为多数元素
        # 本层递归结果: 比较左右两个集合的递归结果, 若结果相同则返回该结果, 若不同则pk, 看哪个结果是本层数组的多数元素
        def helper(start: int, end: int) -> int:
            # start和end为nums起始索引
            # base case
            if start == end:
                return nums[start]

            mid = (end - start) // 2 + start  # 找到当前数组中点
            # 递归左右子数组
            left = helper(start, mid)
            right = helper(mid + 1, end)

            if left == right:
                return left
            else:  # 左右pk
                left_count = sum([1 for i in range(start, end + 1) if nums[i] == left])  # 计算左子数组递归结果在本层出现的次数
                right_count = sum([1 for i in range(start, end + 1) if nums[i] == right])  # 计算右子数组递归结果在本层出现的次数
            return left if left_count > right_count else right

        return helper(0, len(nums) - 1)
