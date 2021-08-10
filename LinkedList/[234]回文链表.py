from .LinkedList import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_node = head
        # 深度优先, 后序遍历, 链表可看做特殊的二叉树
        def dfs(head: ListNode) -> bool:
            if head:
                # 先判断是不是False, 如果为False, 那么最终结果也是False
                if not dfs(head.next):
                    return False
                # 判断对称位置的节点值是否相等, 不相等直接返回False
                # 后序遍历, 所以先判断最后一个非空节点
                if head.val != self.front_node.val:
                    return False
                # 以上两个判断都是True, 前面的节点后移1步
                self.front_node = self.front_node.next
            # head为空, 或者以上判断都为True, 返回True
            return True
        return dfs(head)