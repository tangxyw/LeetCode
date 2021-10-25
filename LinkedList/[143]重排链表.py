from .LinkedList import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 递归
        # 链表长度, 由于只有遍历一次链表才能得到长度, 故先遍历一次整个链表得到总长度, 而把当前链表长度作为参数传递给递归函数
        length = 0
        h = head
        while h:
            length += 1
            h = h.next

        def reorderListHelper(head: ListNode, length: int) -> ListNode:
            """递归函数, 返回值为外层递归对应的尾节点"""
            # base case
            if length == 1:  # 对应总数为奇数个节点, 最后一层递归的输入参数为中间节点
                out_tail = head.next  # out_tail为外层递归的尾结点
                head.next = None  # # 断开中间结点next, 使中间结点为最终链表的最后一个节点
                return out_tail

            if length == 2:  # 对应总数为偶数个节点, 最后一层递归输入参数为靠左的中间结点
                out_tail = head.next.next  # 同len==1
                head.next.next = None
                return out_tail

            # 递归内部
            tail = reorderListHelper(head.next, len - 2)  # tail为本层递归尾部节点, 由下层递归返回值得到
            out_tail = tail.next  # 本层递归尾部节点的next, 需要最后返回给上层递归
            sub_head = head.next  # 下层递归的头结点
            head.next = tail  # 本层递归的头结点的next指向本层递归的尾结点
            tail.next = sub_head  # 本层递归的尾结点的next指向下层递归的头结点
            return out_tail

        # 从head节点开始递归
        reorderListHelper(head, length)
