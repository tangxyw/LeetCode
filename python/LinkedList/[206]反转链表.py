from DoublePointer.LinkedList import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 后序遍历
        # base case
        # 链表为空或者到达最后一个节点
        if not head or not head.next:
            return head
        # 后序遍历, 一直向下递归
        new_node = self.reverseList(head.next)
        # 从倒数第二个节点开始向前
        # 当前节点和下一个节点的前后关系反转
        head.next.next = head
        head.next = None
        # 一直向上返回的都是最后一个节点
        return new_node
