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
                        c=b/a
                stack.append(int(c))
            else:
                stack.append(int(i))
        return stack[0]