from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 单调栈法
        res = {j: -1 for j in nums2}
        s = []  # 定义单调栈, 栈中的元素都是单调递增的
        for i in range(len(nums2) - 1, -1, -1):  # 由后往前遍历nums2
            while s and nums2[i] >= s[-1]:  # 当遍历到的nums2[i]大于等于单调栈s顶部的值, 弹出s顶部的值(这些值在之后的迭代中已经没用了)
                s.pop()
            # 如果s为空, 说明i后面没有比它大的, 不为空, 就取栈顶元素
            res[nums2[i]] = -1 if len(s) == 0 else s[-1]
            s.append(nums2[i])

        return [res[x] for x in nums1]