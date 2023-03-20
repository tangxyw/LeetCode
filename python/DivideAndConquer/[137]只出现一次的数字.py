from typing import List
from random import randint

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 二分法
        # https://leetcode-cn.com/problems/single-number-ii/solution/python3-kuai-su-xuan-ze-fen-zhi-suan-fa-prk3u/
        n = len(nums)
        left, right = 0, n - 1  # 双指针
        while left < right:
            k = randint(left, right)  # 为避免无限循环(例如[1,1,1,2]每次选择最后一个元素), 在左右指针范围内随机选择一个索引
            nums[k], nums[right] = nums[right], nums[k]  # 将随机选择的数字放到右指针位置作为pivot
            i, j = left, right - 1  # i指向左指针, j指向右指针前面位置(pivot前面)
            while i <= j:  # 粗排序, 使得<=pivot的元素在前面, >pivot的元素在后面
                while i <= right - 1 and nums[i] <= nums[right]:
                    i += 1  # 使得i的左边的元素都<=pivot, nums[i] > pivot
                while j >= left and nums[j] > nums[right]:
                    j -= 1  # 使得j的右边的元素都>pivot, nums[j] <= pivot
                if i < j:  # i还在j前面, 交换i和j位置的元素, i和j各自往中间移动1格, 进入下一轮迭代
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            # 上面的迭代完成后, i指向第一个比pivot大的元素位置
            # 把pivot换到i, 使得[left,i]的所有元素都<=pivot, [i+1,right]的所有元素都>pivot
            nums[i], nums[right] = nums[right], nums[i]
            # 判断目标元素在哪个区间
            if (i - left + 1) % 3 != 0:  # [left,i]的长度mod 3不为0, 则目标元素在此区间
                right = i  # 更新左指针
            else:  # 目标元素在[i+1, right]
                left = i + 1  # 更新右指针

        # 最终left和right指向同一个位置, 任选其一返回
        return nums[left]
