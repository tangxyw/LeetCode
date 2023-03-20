from .LinkedList import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 前指针
        self.front_pointer = head

        def helper(head: ListNode):
            # 后序遍历
            # base case
            if not head:
                return True
            # 一直向下递归
            next_res = helper(head.next)
            # 从倒数第一个节点开始
            # 当前节点的后一个节点结果为False, 本层递归结果也为False, 最后抛出到顶层递归结果
            if not next_res:
                return False
            # 当前节点值和对称位置节点值不等, 本层递归结果为False, 最后抛出到顶层递归结果
            if head.val != self.front_pointer.val:
                return False
            # 前指针后移一位
            self.front_pointer = self.front_pointer.next
            # 上述if条件都不符合, 本层递归结果为True
            return True

        return helper(head)
