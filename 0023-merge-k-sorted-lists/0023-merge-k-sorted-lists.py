import heapq
class Solution:
    def mergeKLists(self, lists):
        minHeap = []
        dummy = ListNode(0)
        curr = dummy
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        return dummy.next