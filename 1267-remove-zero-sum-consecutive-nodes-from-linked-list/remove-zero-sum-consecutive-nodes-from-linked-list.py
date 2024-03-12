# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node_map = {}
        cur = head
        prefix_sum = 0
        dummy = ListNode()
        dummy.next = head
        node_map[0] = dummy
        while cur:
            prefix_sum += cur.val
            node_map[prefix_sum] = cur
            cur = cur.next
        cur = dummy
        prefix_sum = 0
        while cur:
            prefix_sum += cur.val
            cur.next = node_map[prefix_sum].next
            cur = cur.next
        return dummy.next



        