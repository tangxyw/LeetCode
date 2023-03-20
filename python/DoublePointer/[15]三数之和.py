from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:  # 当前值大于0, 右边的值肯定也大于0, 不可能相加等于0, 停止循环
                break
            if nums[i] == nums[i - 1] and i > 0:  # 当前值和上一个值相等, 跳过
                continue
            # 左右指针, 指向当前元素后面的第一个和最后一个元素, 这里无需再遍历前面的元素了(会有重复)
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]  # 求和
                if sum == 0:  # 找到一组答案
                    res.append([nums[i], nums[left], nums[right]])
                    # 去重, 左指针左移, 直到与左指针右边的元素不相等, 这时左指针停在与之前元素相等的最后一个元素上
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # 同左指针
                        right -= 1
                    left += 1  # 再左移1步
                    right -= 1  # 再右移1步
                elif sum < 0:
                    while left < right and nums[left] == nums[left + 1]:  # 避免重复计算
                        left += 1
                    left += 1
                elif sum > 0:
                    while left < right and nums[right] == nums[right - 1]:  # 避免重复计算
                        right -= 1
                    right -= 1

        return res
