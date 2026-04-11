class Solution:
    def isValid(self, s: str) -> bool:
        closedict={
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack=[]
        for idx,i in enumerate(s):
            if i in closedict.values():
                stack.append(i)
            elif i in closedict.keys() and stack and stack[-1]==closedict[i]:
                stack.pop()
            else:
                stack.append(i)

        if len(stack)==0:
            return True
        else:
            return False