# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for lst in lists:
            while lst:
                res.append(lst.val)
                lst = lst.next
        if not res:
            return None
        heapify(res)
        dummy = ListNode(0)
        current = dummy
        while res:
            val = heappop(res)
            current.next = ListNode(val)
            current = current.next
        return dummy.next
