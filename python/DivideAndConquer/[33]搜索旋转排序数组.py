from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # 左侧是有序的(注意这里要加=, 因为mid是中间靠左的)
                if nums[left] <= target < nums[mid]:  # target在有序的片段里
                    right = mid - 1
                else:  # target不在有序的片段里
                    left = mid + 1
            else:  # 左侧是无序的, 右侧必是有序的
                if nums[mid] < target <= nums[right]:  # target在有序的片段里
                    left = mid + 1
                else:  # target不在有序的片段里
                    right = mid - 1

        return -1
