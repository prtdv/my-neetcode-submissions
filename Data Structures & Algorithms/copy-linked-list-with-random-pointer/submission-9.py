"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        hmap={None:None}

        while curr: #store each node in hmap, just val, no pointer.
            nNode=Node(curr.val)
            hmap[curr]=nNode
            curr=curr.next

        curr=head
        while curr:
            nNode=Node(0)
            nNode=hmap[curr]
            nNode.next=hmap[curr.next]
            nNode.random=hmap[curr.random]
            curr=curr.next
        
        return hmap[head]