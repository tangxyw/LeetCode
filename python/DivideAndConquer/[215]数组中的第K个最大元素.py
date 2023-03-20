import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(l, r):
            """
               预排序nums[l:r+1]:
               随机取一个元素pivot, 放在正确的降序位置上, 使得pivot左边的元素都<=它, 右边的元素都>=它
            """
            if l >= r:  # base case
                return
            t = random.randint(l, r)  # 选取一个随机索引
            nums[l], nums[t] = nums[t], nums[l]  # pivot放在最左边l位置

            # 定义i, j双指针
            i, j = l, r
            while i < j:
                while i < j and nums[j] <= nums[l]: j -= 1  # 左移j, 直到j右边都<=pivot, j停在>pivot的位置上
                while i < j and nums[i] >= nums[l]: i += 1  # 右移i, 直到i左边都>=pivot, i停在<pivot的位置上
                nums[i], nums[j] = nums[j], nums[i]  # 交换位置i和位置j的元素, 继续迭代
            # 上述迭代完成后, i和j指向的位置相同, 该位置元素>pivot, 交换它们的位置, 使得pivot放在了正确的降序位置
            # 此时,nums的前i+1个任意元素, 都大于等于nums后面任意元素
            nums[l], nums[i] = nums[i], nums[l]
            if k == i + 1:  # 前k个元素已经是最大的k个元素了, 直接返回
                return
            if k < i + 1:  # k小于i+1, 继续在nums的l到i-1区间递归
                quick_sort(l, i - 1)
            if k > i + 1:  # k大于i+1, 继续在nums的i+1到r区间递归
                quick_sort(i + 1, r)

        # 从整个nums的首尾位置开始递归
        quick_sort(0, len(nums) - 1)
        #   递归结束后, 返回nums的第k个元素
        return nums[k - 1]
