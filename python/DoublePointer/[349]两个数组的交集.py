from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        p1, p2 = 0, 0
        res = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                while p1 < len(nums1) and nums1[p1] < nums2[p2]:    # p1移动到下一个不小于num2[p2]的位置
                    p1 += 1

            elif nums1[p1] > nums2[p2]:
                while p2 < len(nums2) and nums1[p1] > nums2[p2]:    # p2移动到下一个不小于num1[p1]的位置
                    p2 += 1

            else:
                if not res or nums1[p1] != res[-1]:  # 检查当前num是否已经在交集中了
                    res.append(nums1[p1])
                p1 += 1
                p2 += 1

        return res
