from CreateTree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def helper(root: TreeNode, presum):
            if not root:
                return
            presum += root.val  # 更新前缀和: 当前节点前缀和+当前节点值
            for key, count in self.presum_cnt.items():  # 遍历前缀和次数字典
                if presum - key == targetSum:  # 依次计算当前前缀和和祖先节点前缀和之差, 当差等于target时, 更新res
                    self.res += self.presum_cnt[key]
            self.presum_cnt.update({presum: self.presum_cnt.get(presum, 0) + 1})  # 更新前缀和次数字典: 当前前缀和次数+1
            helper(root.left, presum)  # 递归左子树
            helper(root.right, presum)  # 递归右子树
            self.presum_cnt[presum] -= 1  # 递归完左右子树后, 要回溯, 确保前缀和次数字典中只存放当前路径的前缀和

        self.presum_cnt = dict({0: 1})  # 存放每个节点前缀和以及出现次数的字典, key为前缀和, value为在同一条路径内的出现次数; 初始化为{0:1}为了单节点val=target的情况
        self.res = 0  # 满足要求的路径数
        helper(root, 0)
        return self.res
