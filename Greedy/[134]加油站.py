from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 贪心
        # https://leetcode-cn.com/problems/gas-station/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--30/
        n = len(gas)
        i = 0  # 起点初始值
        while i < n:  # 遍历每一个位置作为起点
            j = i  # j为i能够到达的最远位置
            remain = gas[i]  # 在位置i加油
            while remain - cost[j] >= 0:  # 判断能够前往下一个位置
                remain += gas[(j + 1) % n] - cost[j]  # 在下一个位置加油, 继续向前, 更新remain
                j = (j + 1) % n  # 环形道路, j可能跑到i前面
                if i == j:  # j回到了i, 直接返回位置i
                    return i
            if j < i:  # j没有回到i, 且j在i前面, 说明i后面的位置都不符合, 直接返回-1
                return -1
            i = j + 1  # 跳过i到j之间的点, 都不符合

        return -1  # 没有找到符合条件的点
