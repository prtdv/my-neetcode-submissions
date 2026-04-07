class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k={}
        j={}

        for i in s:
            k[i]=k.get(i,0)+1
        
        for i in t:
            j[i]=j.get(i,0)+1
        
        if k==j:
            return True
        else: 
            return False