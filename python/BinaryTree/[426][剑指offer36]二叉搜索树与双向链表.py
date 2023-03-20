from CreateTree import TreeNode

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # BST的中序遍历的结果为递增序列
        # 将Node的left节点作为pre, right节点作为next
        def inorder(root: 'Node'):
            if not root:
                return
            inorder(root.left)
            if not self.pre:   # 遍历到第一个节点的特殊逻辑, 这是pre是空
                self.head = root    # 将head指向第一个节点
            else:   # 不是第一个节点
                self.pre.right = root  # pre的下一个节点指向当前节点
                root.left = self.pre    # 当前节点的上一个节点指向pre, 注意这里pre已经完成递归, 当前节点的left节点也完成了递归, 所以修改它们的指向不影响之后的递归
            self.pre = root # 将上一个节点指向当前节点
            inorder(root.right)

        if not root:
            return None
        self.head = None    # head节点指针
        self.pre = None     # 上一个节点指针
        inorder(root)
        self.head.left = self.pre   # 最后将head节点的上一个节点指针指向最后一个节点
        self.pre.right = self.head  # 再将最后一个节点的下一个节点指针指向head节点
        return self.head    # 返回head节点作为结果