from .CreateTree import TreeNode
from ..LinkedList.LinkedList import ListNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/shou-hua-tu-jie-san-chong-jie-fa-jie-zhu-shu-zu-ku/
        # 根据BST的中序遍历结果顺序构造BST
        self.h = head  # 全局变量, 按中序遍历的顺序构造BST
        length = 0  # 链表长度
        while head:
            head = head.next
            length += 1

        return self.bulidBST(0, length - 1)

    def bulidBST(self, start, end):
        # start, end为链表的索引
        if start > end:  # base case, 到达了BST的根节点的下一层
            return None
        mid = (start + end) >> 1  # 找到当前链表中间点, 作为子树根节点
        left = self.bulidBST(start, mid - 1)  # 根据中序遍历顺序, 先递归构建左子树
        root = TreeNode(self.h.val)  # 上面递归返回后, 构建当前递归层根节点(画出递归树有助理解)
        self.h = self.h.next  # h右移
        root.left = left  # 把左子树插到root上
        root.right = self.bulidBST(mid + 1, end)  # 再递归构建右子树
        return root
