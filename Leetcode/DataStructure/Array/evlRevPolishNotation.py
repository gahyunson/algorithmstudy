# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop(-2) + stack.pop()) 
            elif token == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif token == '*':
                stack.append(stack.pop(-2) * stack.pop())
            elif token == '/':
                stack.append(int(stack.pop(-2) / stack.pop()))
            else:
                stack.append(int(token))
            print(token, stack)
        return stack[0]

        # if token[i]==operators:
        #   rep = token[i-2] token[i] token[i-1]

        #  token[i-3] token[i-2] token[i-1] token[i] token[i+1]
        #->token[i-3] token[i-2] token[i] token[i-1] token[i+1] 
        #->token[i-3] token token[i+1] 
        
    
