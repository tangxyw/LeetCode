from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 分治, 二分搜索
        def helper(start, end) -> int:
            # base case, 只剩一个值判断是否为target
            if start == end:
                if nums[start] == target:
                    return start
                else:
                    return -1

            # 升序部分, 由最大最小值判断target是否在该区间内, 相当与剪枝
            if nums[start] < nums[end] and (target < nums[start] or target > nums[end]):
                return -1

            mid = (end - start) // 2 + start  # 取区间中点
            # 左右子数组递归
            left = helper(start, mid)
            right = helper(mid + 1, end)
            return max(left, right)  # 若都没找到就是-1, 找到了就是target索引

        return helper(0, len(nums) - 1)