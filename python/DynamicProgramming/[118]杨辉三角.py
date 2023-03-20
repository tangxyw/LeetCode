from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 直接递推
        # dp[i]为numRows=i+1的杨辉三角最后一行的结果
        dp = [1]
        res = [dp]
        for i in range(1, numRows):
            new_dp = [0] * (len(dp)+1)  # 需要增加的一行的元素数, 为上一个杨辉三角结果最后一行元素数+1
            new_dp[0], new_dp[-1] = 1, 1    # 最左最右都是1
            for j in range(1, len(new_dp)-1):   # 计算中间的数字
                new_dp[j] = dp[j-1] + dp[j]
            res.append(new_dp)  # 加入结果集
            dp = new_dp # 保持dp为最后一行
        return res
