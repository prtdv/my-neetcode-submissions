class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        final=""
        char=[]
        for i in s:
            if i.isalnum():
                char.append(i)

        final="".join(char)
        if final[::-1]==final[::1]:
            return True
        else:
            return False