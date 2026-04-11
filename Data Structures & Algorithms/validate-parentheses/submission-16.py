class Solution:
    def isValid(self, s: str) -> bool:
        closedict={
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack=[]
        for i in s:
            if i in closedict.values():
                stack.append(i)
            if i in closedict:
                if len(stack)!=0 and stack[-1]==closedict[i]:
                    stack.pop()
                else:
                    stack.append(i)
            
        if not stack:
            return True
        else:
            return False