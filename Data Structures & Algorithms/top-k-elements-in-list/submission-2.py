class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm={}
        for i in nums:
            if i in hashm:
                hashm[i]+=1
            else:
                hashm[i]=1
        
        max_counts=[]

        counts=list(hashm.values())
        counts.sort(reverse=True)

        for i in range(0,k):
            max_counts.append(counts[i]) #i now have the frequencies of max k elements. i just need those elements now.
        
        keys=[]

        for i in max_counts:
            for k in hashm.keys():
                if hashm[k]==i and k not in keys:
                    keys.append(k)
        
        return list(keys)



        
            
        
            