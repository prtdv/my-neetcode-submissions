class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                y=int(stack.pop())
                x=int(stack.pop())
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
                
            print(stack)
        return stack[0]

        