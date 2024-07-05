# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indices = []
        prev = head
        head = head.next
        mid = head
        midIndex = 1
        head = head.next

        while head:
            m = mid.val
            p = prev.val
            h = head.val
            if m<p and m<h:
                indices.append(midIndex)
            elif m>p and m>h:
                indices.append(midIndex)
            prev = prev.next
            mid = mid.next
            midIndex+=1
            head = head.next
        
        if len(indices)<2: return [-1,-1]
        minDist = min(indices[a] - indices[a-1] for a in range(1, len(indices)))
        return([minDist, indices[-1] - indices[0]])
