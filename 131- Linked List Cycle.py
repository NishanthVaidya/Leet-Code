class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        visited = {}
        temp = head
        
        while temp:
            if temp in visited:
                return True
            visited[temp] = True
            temp = temp.next
        
        return False
