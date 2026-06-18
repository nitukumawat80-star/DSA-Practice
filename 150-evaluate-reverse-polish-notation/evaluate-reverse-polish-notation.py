from math import ceil , floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-/*":
                b , a = stack.pop() , stack.pop()
                if t == '+':
                    stack.append(a+b)

                elif t == '-':
                    stack.append(a-b)

                elif t == '*':
                    stack.append(a*b)
                else:
                    division = int(a / b)
                    
                    stack.append((division))
                   

            else:
                stack.append(int(t))

        return stack[0]
                    

        