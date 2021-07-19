from CreateTree import TreeNode

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        # BST的中序遍历, 结果为递增序列
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            self.cur = root.val # 当前节点值赋值到cur
            if self.pre is None:    # 遍历到第一个节点时的特殊逻辑
                self.cur_count = 1
            elif self.pre == self.cur:  # 当前节点值和上一个节点值相等, cur_count
                self.cur_count += 1
            else:   # 当前节点值和上一个节点值不相等, cur_count重置为1
                self.cur_count = 1
            if self.cur_count == self.max_count:    # 当前节点值计数与最大计数相等, 把当前节点值添加到当前众数列表里
                self.cur_mode.append(self.cur)
            elif self.cur_count > self.max_count:   # 当前节点值技术大于最大技术, 重置当前众数列表为[cur], 更新max_count
                self.cur_mode = [self.cur]
                self.max_count = self.cur_count
            self.pre = self.cur # 上一个节点值更新
            inorder(root.right)

        if not root:
            return []
        self.cur = None   # 当前遍历到的节点值
        self.pre = None   # 上一个遍历到的节点值
        self.cur_count = 0  # 当前遍历到的节点值出现的次数
        self.cur_mode = [] # 当前众数
        self.max_count = 0  # 节点值最大出现次数
        inorder(root)
        return self.cur_mode