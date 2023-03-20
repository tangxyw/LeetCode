from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        n = len(nums)
        # 第一次遍历, 将所有0移动到nums最左侧
        for i in range(n):
            if nums[i] == 0:    # 遇到0
                if i > p:   # 如果i和p指向同一个元素就无需交换
                    nums[i], nums[p] = nums[p], nums[i]
                p += 1  # 只要找到1个0, p就右移1步

        # 第二次遍历, 将所有1移动到0后面
        for j in range(p, n):
            if nums[j] == 1:    #遇到1
                if j > p:   # 如果j和p指向同一个元素就无需交换
                    nums[j], nums[p] = nums[p], nums[j]
                p += 1  # 只要找到1个1, p就右移1步