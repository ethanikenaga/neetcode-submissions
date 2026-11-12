# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        node = head
        if head == None:
            return False
        while node.next != None:
            if node in seen:
                return True
            seen.add(node)
            node = node.next
        return False

        