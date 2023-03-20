from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 先排序, 升序
        nums1.sort()
        nums2.sort()

        res = []
        # 双指针
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):  # 直到走到其中1个数组的尾部
            if nums1[p1] < nums2[p2]:  # 指针指向的数字nums1较小, p1右移1步
                p1 += 1
            elif nums1[p1] > nums2[p2]:  # 指针指向的数字nums2较小, p2右移1步
                p2 += 1
            elif nums1[p1] == nums2[p2]:  # 指针指向的数字相等, 该数字进入交集集合, p1p2都右移1步
                res.append(nums1[p1])
                p1 += 1
                p2 += 1

        return res
