from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_distance = float('inf')
        res = None

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # 遇到重复的数字直接跳到下一个数字
                continue
            # 双指针
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 == target:
                    return sum3
                elif sum3 < target:
                    if target-sum3 < min_distance:
                        min_distance = target-sum3
                        res = sum3
                    while left < right and nums[left] == nums[left+1]:  # 跳过和左指针相同的数字
                        left += 1   # 这时左指针还停留在与前左指针指向相同的最靠右的数字
                    left += 1   # 更新内循环下一次的左指针
                elif sum3 > target:
                    if sum3-target < min_distance:
                        min_distance = sum3-target
                        res = sum3
                    while left < right and nums[right] == nums[right-1]:    # 逻辑与更新左指针相同
                        right -= 1
                    right -= 1

        return res