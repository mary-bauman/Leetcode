# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        cur = newHead
        head = head.next
        total = 0
        while head:
            if head.val==0:
                cur.next = ListNode(total)
                total = 0
                cur = cur.next
            else: total+=head.val
            head = head.next
        return newHead.next
