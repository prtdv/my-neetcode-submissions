class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashm={}

        for i in range(0,len(strs)):
            key="".join(sorted(strs[i]))

            if key not in hashm:
                hashm[key]=[strs[i]]
            else:
                hashm[key].append(strs[i])
        return list(hashm.values())






        

        