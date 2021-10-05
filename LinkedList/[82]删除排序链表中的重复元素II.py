from .LinkedList import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy  # cur初始化为哑元节点, 保证在迭代中, cur的值不会等于后面节点的值

        while cur.next and cur.next.next:  # 遍历直到倒数第三个节点
            if cur.next.val == cur.next.next.val:  # cur的后两个节点值相等时
                cur_val = cur.next.val
                while cur.next and cur.next.val == cur_val:
                    cur.next = cur.next.next  # 直到cur.next指向值不等于cur_value的节点
            else:
                cur = cur.next

        return dummy.next
