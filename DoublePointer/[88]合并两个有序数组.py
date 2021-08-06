from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m - 1  # 指向num1的末尾
        q = n - 1  # 指向num2的末尾
        tail = m + n - 1  # 指向扩展后nums1的末尾

        while tail >= 0:
            # 以下四种情况互斥
            # 每一次迭代比较nums1和nums2的末尾, 将较大者赋值到tail处
            # 由于tail肯定不会跑到p的左边, 所以不必对p和tail之间的元素做任何处理
            if p == -1:  # nums1的所有数值都已经遍历过
                nums1[tail] = nums2[q]  # 将余下的nums2的所有数值依次赋值到tail处
                q -= 1
            elif q == -1:  # 同上
                nums1[tail] = nums1[p]
                p -= 1
            elif nums1[p] >= nums2[q]:  # nums1和nums2都没遍历完, 比较两个数组的末尾数值
                nums1[tail] = nums1[p]
                p -= 1
            elif nums1[p] < nums2[q]:  # 同上
                nums1[tail] = nums2[q]
                q -= 1
            tail -= 1  # 每轮迭代tail都往左移动1格
