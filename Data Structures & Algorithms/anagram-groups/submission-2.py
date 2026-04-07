class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=defaultdict(list)
        
        for i in strs:
            new="".join(sorted(i))
            res[new].append(i)

        return list(res.values())






        

        