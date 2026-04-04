# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        curr = head
        n = 1
        while curr.next:
            n += 1
            curr = curr.next
        curr.next = head
        m = n - (n % k)

        i = 0
        curr = head
        prev = None
        while i < m:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = None
        head = curr
        return head            

