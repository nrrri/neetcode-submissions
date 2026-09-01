# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        while curr: # to check current is not null
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next # set to next value
        return False # not cycle

        """
        what it wants
            - return true if it's cycle liked list
            - check linked list is cycle
            - val.next has the same value can be found only 2 times (cycle)
            - index = cycle count
        what to check
            - check cycle if val = val.next -> cycle
            
        how
            - check if head is not None
            - check if current has not seen
                if seen -> cycle
            - if not set new seen 
            - set current to next
            - loop
        """
        