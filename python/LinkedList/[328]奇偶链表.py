from .LinkedList import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # 链表节点数在2个以下, 直接返回
            return head

        p = head  # 奇数索引指针
        q = head.next  # 偶数索引指针
        head_even = q  # 第一个偶数索引

        while q and q.next:  # 遍历链表
            p.next = q.next  # 奇数node的下一个指针, 指向偶数node的下一个节点
            p = q.next  # 更新奇数索引指针
            q.next = p.next  # 偶数node的下一个指针, 指向奇数node(已更新)的下一个节点
            q = p.next  # 更新偶数索引指针

        p.next = head_even  # 首尾相连
        return head
