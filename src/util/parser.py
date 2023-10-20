from src.array_op.containers import Stack
#GLOBAL CONSTANT
PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '%': 3,
    '^': 3,
    '(': 0,
    ')': 0
}
"""
@brief    Parser for mathematical equations that uses postfix stack implementation
"""
class parser:
    def __init__(self, string, vars={}):
        self.expression = self.__post_fix_parse(string)
        self.var = vars

    def __post_fix_parse(self, expression):
        processed_exp = expression.strip()
        postfix = ""
        stack = Stack()
        for i in processed_exp:
            if PRECEDENCE.get(i) is None: #if it is an operand
                postfix += i
            else: #if it is not an operand
                if(i != ')'):
                    if(stack.isEmpty() or i == '('):
                        stack.push_back(i)
                    elif PRECEDENCE.get(stack.peek()) < PRECEDENCE.get(i):
                        stack.push_back(i)
                    else: # <=
                        while not stack.isEmpty() and PRECEDENCE.get(stack.peek()) >= PRECEDENCE.get(i):
                            postfix += stack.peek()
                            stack.pop_back()
                        stack.push_back(i)
                else:
                    while(stack.peek() != '('):
                        if (stack.peek() != '('):
                            postfix += stack.peek()
                        stack.pop_back()
                    stack.pop_back()
        while not stack.isEmpty():
            if (stack.peek() != '('):
                postfix += stack.peek()
            stack.pop_back()
        return postfix

    def getPostOrderExpression(self):
        return self.expression

    def evaluate(self):
        stack = Stack()
        for i in self.expression:
            if PRECEDENCE.get(i) is None:  # if it is an operand
                stack.push_back(i)
            else:
                operand2 = stack.peek()
                if self.var.get(str(operand2)) is not None:
                    operand2 = self.var.get(str(operand2))
                stack.pop_back()
                operand1 = stack.peek()
                if self.var.get(str(operand1)) is not None:
                    operand1 = self.var.get(str(operand1))
                stack.pop_back()
                result = eval(str(operand1)+i+str(operand2))
                stack.push_back(result)
        return stack.peek()



