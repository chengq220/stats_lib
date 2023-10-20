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
        while not stack.isEmpty():
            if (stack.peek() != '('):
                postfix += stack.peek()
            stack.pop_back()
        return postfix

    def getExpression(self):
        return self.expression

