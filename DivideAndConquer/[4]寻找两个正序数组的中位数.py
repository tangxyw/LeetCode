from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 转化为求两个有序数组合并后的第k小的数, 类似二分搜索
        # 两数组长度和m+n为奇数时, k = (m+n) // 2 + 1
        # 两数组长度和m+n为偶数时, k = (m+n) // 2， k+1 = (m+n) // 2 + 1， 求的是两者的均值
        def getKth(nums1, start1, nums2, start2, k) -> int:
            """返回nums1[start1]和nums2[start2]合并后第k小的数"""
            print(nums1[start1:], nums2[start2:], k)
            if not nums1[start1:] or not nums2[start2:]:    # 其中一个数组为空, 直接返回另一个的第k个数
                return nums1[start1+k-1] if not nums2[start2:] else nums2[start2+k-1]
            if k == 1:  # 返回两个数组第一个元素的较小者
                return min(nums1[start1], nums2[start2])

            len1 = len(nums1[start1:])
            len2 = len(nums2[start2:])

            # 在num1[start1:]和nums2[start2:]中删除k//2个数
            # i,j为两数组待比较位置的索引, 这里要考虑数组长度小于k//2的情况
            i = start1 + min(len1, k // 2) - 1
            j = start2 + min(len2, k // 2) - 1

            if nums1[i] > nums2[j]: # 删掉num[start2:]前面的j+1-start2个元素, 向下递归
                return getKth(nums1, start1, nums2, j+1, k-(j+1-start2))
            else:   # 同上
                return getKth(nums1, i+1, nums2, start2, k-(i+1-start1))

        m = len(nums1)
        n = len(nums2)

        if (m+n) % 2 == 1:  # 两数组长度为奇数
            return getKth(nums1, 0, nums2, 0, (m+n)//2+1)
        else:   # 两数组长度为偶数
            return (getKth(nums1, 0, nums2, 0, (m+n)//2) + getKth(nums1, 0, nums2, 0, (m+n)//2+1)) / 2