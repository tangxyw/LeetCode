from .LinkedList import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 双指针
        # 先判断链表中是否存在环
        # 设计一个慢指针一个快指针, 慢指针每次走1步, 快指针每次走2步
        # 若链表中含有环, 则慢指针和快指针会在环内部相遇
        # 证明:
        # 假设慢指针走了k步, 那么快指针就走了2k步
        # 是否存在正整数k, 满足:
        # 2k = m + a*n + c
        #  k = m + b*n + c
        # m为head到环起点的步数, n为环内步数, a和b为在环内走的圈数, c为在环内走的不足一圈的步数, a>b, 0<=c<n, m>=0
        # 两式相减等到: k = (a-b)*n
        # 这就证明了存在这样的k, 且k是n的整数倍
        # 所以为了等式成立, m+c也必为n的整数倍
        # 为了找到环起点, 在快慢指针相遇时, 讲其中一个指针指向head, 两个指针再次一起走, 步幅都为1, 再次相遇时, 两指针必都走了m步, 相遇点为环起点

        slow = head
        fast = head
        while True:
            if not fast or not fast.next:  # 没有环结构
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # 指针相遇
                break

        # 将其中一个指针指向head
        slow = head
        while slow != fast:
            # 一起走, 直到相遇
            slow = slow.next
            fast = fast.next

        return slow