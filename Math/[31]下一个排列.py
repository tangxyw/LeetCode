from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/

        if len(nums) == 1:
            return

        # 第一次从后向前遍历, 寻找第一个升序对
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:  # 整个nums是降序的, 也就是最大的排列了, 翻转并返回
            nums.reverse()
            return

        k = i - 1
        j = len(nums) - 1
        while j > k and nums[j] <= nums[k]:  # 从后向前, 找到k后面第一个比nums[k]大的(必然能找到), 交换
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]

        # k之后的子数组必然是降序的, 翻转后变为升序
        left = i
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return