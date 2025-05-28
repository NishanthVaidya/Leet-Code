# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Compute length to avoid unnecessary rotations
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        k %= length
        if k == 0:
            return head

        while k > 0:
            current = head
            while current.next and current.next.next:
                current = current.next
            # Rotate last node to front
            last = current.next
            current.next = None
            last.next = head
            head = last
            k -= 1

        return head
