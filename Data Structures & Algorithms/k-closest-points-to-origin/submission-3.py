class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        disttopoint=defaultdict(list)

        for i in points:
            dist=((i[0] - 0)**2 + (i[1] - 0)**2)**(1/2)
            disttopoint[dist].append(i)
        print("disttopoint: ", disttopoint)

        heap=[]
        for dist in disttopoint:
            heapq.heappush(heap, dist)
        print("heap: ",heap)

        ans=[]
        while k>0:
            key=heapq.heappop(heap)
            print(disttopoint[key])
            for closest in disttopoint[key]:
                ans.append(closest)
                k-=1
                
        return ans

        