from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 原地哈希法, 将nums[i]都放到nums[nums[i]-1]上, 1 <= nums[i] <= n
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:  # 不断地将nums[i]放到索引nums[i]-1上
                j = nums[i] - 1  # nums[i]应该在的位置
                nums[i], nums[j] = nums[j], nums[i]

        # 再遍历一次, 看哪一个位置上的数字不「正确」
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 所有位置都正确, 这时nums为[1,2,3,4,...,n], 返回n+1
        return n + 1
