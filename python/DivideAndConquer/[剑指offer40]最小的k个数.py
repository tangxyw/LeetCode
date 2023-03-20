from typing import List
import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quick_sort(l, r):
            """
               预排序arr[l:r+1]:
               随机取一个元素pivot, 放在正确的升序位置上, 使得pivot左边的元素都<=它, 右边的元素都>=它
            """
            if l >= r:  # base case
                return
            t = random.randint(l, r)  # 选取一个随机索引
            arr[l], arr[t] = arr[t], arr[l]

            # 定义i, j双指针
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1  # 左移j, 直到j右边都>=pivot, j停在<pivot的位置上
                while i < j and arr[i] <= arr[l]: i += 1  # 右移i, 直到i左边都<=pivot, i停在>pivot的位置上 
                arr[i], arr[j] = arr[j], arr[i]  # 交换位置i和位置j的元素, 继续迭代
            # 上述迭代完成后, i和j指向的位置相同, 该位置元素<pivot, 交换它们的位置, 使得pivot放在了正确的升序位置
            # 此时,arr的前i+1个元素任意元素, 都小于arr后面任意元素
            arr[l], arr[i] = arr[i], arr[l]
            if k == i + 1:  # 前k个元素已经是最小的k个元素了, 直接返回
                return
            if k < i + 1:  # k小于i+1, 继续在arr的l到i-1区间递归 
                quick_sort(l, i - 1)
            if k > i + 1:  # k大于i+1, 继续在arr的i+1到r区间递归
                quick_sort(i + 1, r)

        #   从整个arr的首尾位置开始递归
        quick_sort(0, len(arr) - 1)
        #   递归结束后, 返回arr的前k个元素
        return arr[:k]
