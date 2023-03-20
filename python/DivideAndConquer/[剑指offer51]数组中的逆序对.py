from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 每个递归函数中都要开辟的临时存储空间, 存储数据为左右子数组首尾拼接
        tmp = [None] * len(nums)

        def merge_sort(l, r):
            """升序排序nums[l:r+1], 返回nums[l:r+1]内的所有逆序对数量"""
            # base case
            if l >= r:  # 这里用>=判断, 是为了包括nums为[]的情况
                return 0
            # 分治法
            m = l + (r - l) // 2
            # 后序遍历
            # 当前nums[l,r+1]逆序对数量的第一部分, 来源于左右子数组的逆序对数之和
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 此时nums[l,m+1]和nums[m+1:r+1]已经排好序
            tmp[l:r + 1] = nums[l:r + 1]
            i, j = l, m + 1  # i,j初始化为左右子数组的第一个索引
            for k in range(l, r + 1):  # 遍历nums[l:r+1]
                # 分四种情况讨论
                # 1.左数组遍历完毕, 将右数组剩余部分依次填入nums[l:r+1]剩余部分
                if i == m + 1:
                    nums[k] = tmp[j]
                    j += 1
                # 2.右数组遍历完毕, 将左数组剩余部分依次填入nums[l:r+1]剩余部分
                elif j == r + 1:
                    nums[k] = tmp[i]
                    i += 1
                # 3.左右数组都未遍历完毕, 当前左数组指针 <= 当前右数组指针, 则将较小的左数组指针填入nums[k]
                elif tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                # 4.左右数组都未遍历完毕, 当前左数组指针 > 当前右数组指针, 则将较小的右数组指针填入nums[k]
                else:
                    nums[k] = tmp[j]
                    j += 1
                    # 这时左数组中i到m之间的所有数都和tmp[j]构成了逆序对, 加到res上
                    res += m - i + 1

            return res

        return merge_sort(0, len(nums) - 1)
