
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next    

        for _ in range(right - left):
            Next = curr.next
            curr.next = Next.next
            Next.next = prev.next
            prev.next = Next


        return dummy.next            

     
       
