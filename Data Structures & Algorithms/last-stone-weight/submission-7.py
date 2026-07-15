class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.minHeap=[]
        for i in stones:
            heapq.heappush(self.minHeap,-i)

        while len(self.minHeap)>1:
            x=-heapq.heappop(self.minHeap)
            y=-heapq.heappop(self.minHeap)
            if x==y:
                pass
            elif x>y:
                heapq.heappush(self.minHeap,-abs(y-x))
            print(self.minHeap)
        if len(self.minHeap)==0:
            return 0
        return -heapq.heappop(self.minHeap)

