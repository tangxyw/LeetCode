from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # A与B相邻, A在B左边
        # 左规则: A得分 < B得分时, B糖果 > A糖果
        # 右规则: A得分 > B得分时, A糖果 > B糖果
        # 评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果 当且仅当 糖果分配同时满足左规则和右规则

        n = len(ratings)
        # 满足左规则时, 所需最少糖果数量
        left = [1] * n  # 每个人至少分配1颗糖果
        for i in range(n):
            if i > 0 and ratings[i - 1] < ratings[i]:
                left[i] = left[i - 1] + 1

        # 满足右规则时, 所需最少糖果数量
        right = [1] * n
        for j in range(n - 1, -1, -1):  # 这时要从后往前遍历ratings
            if j < n - 1 and ratings[j] > ratings[j + 1]:
                right[j] = right[j + 1] + 1

        # 要同时满足左右规则, 每个位置取左规则和右规则数组中对应位置的较大值
        # 证明1: 上述方法得到的数组为问题解
        #        A得分 < B得分时, left[A] < left[B], right[A] == 1 <= right[B],
        #        故max(left[A], right[A]) == left[A], max(left[B], right[B]) >= left[B] > left[A], 满足左规则
        #        同理可证也满足右规则
        # 证明2: 上述方法得到的数组为问题最优解
        #        反证法, 若上述方法得到的数组不为最优解, 最优解数组为a, 则必有在某个位置C, 有a[C] < max(left[C], right[C])
        #        不是一般性, 令a[C] < left[C], 而left为左规则的最优解, 故a不符合左规则, 矛盾
        res = 0
        for k in range(n):
            res += max(left[k], right[k])
        return res
