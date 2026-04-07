class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s)-1

        while l<=r:
            if not s[l].isalnum():
                l+=1
                continue #need to move to the next iteration, if there are 2 consequetive alnums would cause issue as it's moves to the comparision statement.
            if not s[r].isalnum():
                r-=1
                continue
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True

                