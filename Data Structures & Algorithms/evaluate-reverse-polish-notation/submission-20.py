class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        evals=["+","-","*","/"]

        for i in tokens:
            if i in evals:
                a=int(stack.pop())
                b=int(stack.pop())
                match i:
                    case "+":
                        c=a+b
                    case "-":
                        c=b-a
                    case "*":
                        c=b*a
                    case "/":
                        c=int(b/a)
                stack.append(c)
            else:
                stack.append(int(i))
        print(stack)
        return stack[0]