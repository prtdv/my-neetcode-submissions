class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/": #isnumeric() only returns true for +ve nums
                stack.append(int(tokens[i]))
            else:
                y=stack.pop()
                x=stack.pop()
                match tokens[i]:
                    case '+':
                        c=x+y
                    case '-':
                        c=x-y
                    case '*':
                        c=x*y
                    case '/':
                        c=int(x/y)
                stack.append(c)
                
        return stack[0]

        