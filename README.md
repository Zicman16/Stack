Stack Explanations

  Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true


Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

	My Code:

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

                #checks to see if the 

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

        # Check status of stack. if stack isn't empty, there's an issue, in this case return false.
        if len(Stack) == 0:
            return True 
        else:
            return False


Explanation: 
Iterate through the given string, adding each character into the stack.
When a close parenthesis character is hit (  “)”, “}”, “]”   ), we stop, and pop out the previous item in the stack.

If the previous character is the valid partner of the current closed parenthesis, we continue iterating through the string.

If the previous character isn’t the valid partner, we return false.

If we make it all of the way to the end of the string in the for loop, we return true.



  Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in reverse Polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

My Code: 

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

Explanation: 

Step 1: Create a stack.

Step 2: Enter values into the stack

Iterate through the tokens. If the token represents a number, put it into the stack.

If an operand is detected, pop out the last two elements of the stack and perform the necessary operation. Add the result into the stack.

	Step 3: Return the result.

Once all of the tokens have been iterated through, the final answer should be all that remains. Return this value using the first index.

