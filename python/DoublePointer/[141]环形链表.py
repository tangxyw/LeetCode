from LinkedList import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        # 快慢指针
        fast = head
        slow = head
        while fast and fast.next:  # 因为while内部引用了fast.next.next，故这里fast和fast.next都要不为None, 否则循环内部报错
            fast = fast.next.next  # 快指针每次走两步
            slow = slow.next  # 慢指针每次走一步
            if fast == slow:  # 若快慢指针能够相遇, 则链表存在环
                return True

        return False
