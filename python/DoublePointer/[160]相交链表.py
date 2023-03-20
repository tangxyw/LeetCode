from LinkedList import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 双指针分别指向两个链表的head
        pa = headA
        pb = headB
        while pa != pb:  # 如果有相交, 则pa==pb时就是交点, 如果无交点, pa和pb最后都是None(这时也有pa==pb)
            pa = pa.next if pa else headB  # pa每次走1步, 走到尾部时, 转向B的head
            pb = pb.next if pb else headA  # 同上

        return pa
