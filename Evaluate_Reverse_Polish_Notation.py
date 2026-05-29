class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        n = len(tokens)
        for i in range(n):

            if tokens[i] == "*":

                element_2 = int(stack.pop())
                element_1 = int(stack.pop())
                ans = element_1 * element_2
                stack.append(ans)

            elif tokens[i] == "+":

                element_2 = int(stack.pop())
                element_1 = int(stack.pop())
                ans = element_1 + element_2
                stack.append(ans)

            elif tokens[i] == "-":

                element_2 = int(stack.pop())
                element_1 = int(stack.pop())
                ans = element_1 - element_2
                stack.append(ans)

            elif tokens[i] == "/":

                element_2 = int(stack.pop())
                element_1 = int(stack.pop())
                ans = int(element_1 / element_2)
                stack.append(ans)

            else:
                stack.append(int(tokens[i]))

        return stack[0]





Sol = Solution()

# Tokens = ["2","1","+","3","*"]

# Tokens = ["4","13","5","/","+"]

Tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

Res = Sol.evalRPN(Tokens)
print(Res)



