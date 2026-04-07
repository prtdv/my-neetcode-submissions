class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k={} #stores (char:count)
        j={}

        if len(s)!=len(t):
            return False

        for i in range(0,len(s)):
            k[s[i]]=k.get(s[i],0)+1
            j[t[i]]=j.get(t[i],0)+1

        if k==j:
            return True
        else:
            return False
