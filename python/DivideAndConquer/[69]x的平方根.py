class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分搜索
        # 由于结果必然存在, 故无需考虑不存在的情况
        # x的算术平方根一般不大于x//2, 0和1是例外
        if x == 0 or x == 1:
            return x

        left = 1
        right = x // 2
        while left <= right:  # 从[1, x//2]为起点开始搜索, 相当于左右都闭
            mid = (right - left) // 2 + left  # 区间中点
            if mid <= x // mid and mid + 1 > x // (mid + 1):  # 必然能找到结果
                return mid
            elif mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1
