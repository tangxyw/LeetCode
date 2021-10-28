from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 双指针
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                while left < right and numbers[left] == numbers[left + 1]:  # 跨过重复的组合
                    left += 1
                left += 1
            elif numbers[left] + numbers[right] > target:
                while left < right and numbers[right] == numbers[right - 1]:  # 跨过重复的组合
                    right -= 1
                right -= 1
