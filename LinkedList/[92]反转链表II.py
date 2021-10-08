from .LinkedList import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 头插法
        # https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/java-shuang-zhi-zhen-tou-cha-fa-by-mu-yi-cheng-zho/
        dummy = ListNode(-1)
        dummy.next = head

        # 先找到反转区间前面一个节点, 设为g
        g = dummy
        for _ in range(left - 1):
            g = g.next

        # g的下一个节点为反转区间的第一个节点, 设为p, 反转后应当在区间最后, 每次迭代把p后面的节点移动到p前面, 即头插法
        p = g.next
        for _ in range(right - left):  # 要移动right-left个节点
            tmp = p.next  # 定义p后面一个节点为tmp
            p.next = tmp.next  # 把p的下一个节点指向后面的后面节点
            tmp.next = g.next  # tmp放到反转区间最前面(注意这里不能把g.next写成p, 因为在第1次迭代后, g.next就不是p了)
            g.next = tmp  # 上一步的延续, g后面链接上tmp

        return dummy.next
