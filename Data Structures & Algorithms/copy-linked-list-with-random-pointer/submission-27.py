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

        while curr:
            copy=Node(curr.val) #copies only values, null pointers.
            hmap[curr]=copy #makes a hmap with only nodes having vals and null pointers
            curr=curr.next
        
        curr=head
        while curr:
            nNode=hmap[curr] #copies the entire node class structure. only val, null pointers.
            nNode.next=hmap[curr.next]
            nNode.random=hmap[curr.random]
            curr=curr.next
        
        return hmap[head]