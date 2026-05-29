class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        closedParentheses = ")]}"

        for i in s:

            # check to see if it is a closed parenthesis, if so, pop out the last in the stack.
            #  if it a valid partner, continue
            #  if not, return false.
            if i in closedParentheses:

                # if the stack is empty, it is impossible to have a valid parenthesis, so we return false.
                if len(Stack) == 0:
                    return False
                else:
                    partner = Stack.pop()

                #checks to see if the there is a valid partnership. If so, we continue, if not, return false.

                if i == ")" and partner == "(":
                    continue

                elif i == "]" and partner == "[":
                    continue

                elif i == "}" and partner =="{":
                    continue

                else:
                    return False
                
            else:
                Stack.append(i)

        # Check status of stack. if stack isn't empty, there's an issue. in this case return false.

        if len(Stack) == 0:
            return True
        
        else:
            return False






Sol = Solution()

### Test cases 
# S = "()[]{}"
#S = "()"
#S = "(]"
S = ([])
#S = "([)]"

# S = "["

res = Sol.isValid(S)
print(res)
