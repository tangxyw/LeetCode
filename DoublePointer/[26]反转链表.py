from LinkedList import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 双指针
        pre = None  # 前面的指针, 初始化指向反转后的末尾None
        cur = head  # 后面的指针, 初始化指向反转后的最后一个节点head
        while cur:  # 每一轮迭代后, pre和cur都在原链表上后移1步
            tmp = cur.next  # 首先记录cur的下一个节点作为缓存
            cur.next = pre  # 局部反转
            pre = cur   # pre右移
            cur = tmp   # cur右移
        return pre