class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        final=""
        for i in s:
            if i.isalnum():
                final+=i
        if final[::-1]==final[::1]:
            return True
        else:
            return False