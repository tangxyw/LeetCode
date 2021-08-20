import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums: List[int], left, right):
            """将nums[left:right+1]中的某一个随机元素放到正确的降序排列位置上, 并返回位置索引"""
            if left == right:
                return left
            seed = random.randint(left, right)  # 选取一个随机索引
            nums[left], nums[seed] = nums[seed], nums[left]  # 再放到nums[left]位置上
            pivot = nums[left]

            i = left  # 指针i先指向pivot
            for j in range(left + 1, right + 1):  # 指针j从pivot后面开始遍历
                if nums[j] > pivot:  # 只要遇到比pivot大, 就依次把它放到pivot后面
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
            # 上述遍历完成后, i指向最后一个比pivot大的元素, 交换它和pivot的位置, pivot就被放到了正确的排序位置上
            # 此时pivot左边的元素都比它大, 右边的元素都小于等于它
            nums[left], nums[i] = nums[i], nums[left]
            return i

        # 双指针
        left = 0
        right = len(nums) - 1
        while left <= right:
            print(nums)
            index = partition(nums, left, right)  # 在指针范围内排序一个元素
            print(index)
            if index == k - 1:  # 由于index从0开始, 所以这里是k-1
                return nums[index]  # 找到了就返回
            elif index < k - 1:  # 找打了更大的数, 下一步在这个数的右边区间里找
                left = index + 1
            elif index > k - 1:  # 找到了更小的数, 下一步在这个数的左边区间里找
                right = index - 1

        """
        另一种方法
        pivot = nums[0]
        equal = [x for x in nums if x == pivot]
        lower = [x for x in nums if x < pivot]
        greater = [x for x in nums if x > pivot]
        if not lower and not greater:
            return pivot

        if len(greater) == k-1:
            return pivot
        elif len(greater) > k-1:
            return self.findKthLargest(greater, k)
        elif len(greater) < k-1:
            if len(greater)+len(equal) >= k:
                return pivot
            else:
                return self.findKthLargest(lower, k-len(greater)-len(equal))
        """
