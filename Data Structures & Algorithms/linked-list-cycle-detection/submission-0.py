# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        visited={}
        while curr:
            if curr in visited:
                visited[curr]=1
                return True
            visited[curr]=0
            curr=curr.next

        return False
        