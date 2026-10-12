class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=['+', '-', '*', '/']

        for i in tokens:
            if i in operations:
                b=stack.pop()
                a=stack.pop()
                match i:
                    case '+':
                        c=a+b
                    case '-':
                        c=a-b
                    case '*':
                        c=a*b
                    case '/':
                        c=int(a/b)
                stack.append(c)
            else:
                stack.append(int(i))
        if len(stack)==1:
            return stack[0]

            



