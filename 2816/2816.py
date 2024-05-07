class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        while head:
            num = (num*10) + int(head.val)
            head = head.next
        sys.set_int_max_str_digits(50000)
        s = str(num*2)
        newHead = ListNode(s[0])
        s = s[1:]
        cur = newHead
        while s:
            cur.next = ListNode(s[0])
            s = s[1:]
            cur = cur.next
        return newHead
