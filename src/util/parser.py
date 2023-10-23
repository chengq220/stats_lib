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
    def __init__(self, string, key=None, value=None):
        self.expression = self.__post_fix_parse(string)
        self.key = key
        self.value = value


    def __post_fix_parse(self, exp): #doesn't work for expression for things bigger than single digits
        postfix = ""
        stack = Stack()
        i = 0
        while(i < len(exp)):
            c_exp = ""
            while(exp[i] != " "):
                c_exp += exp[i]
                i = i+1
            i = i+1
            if PRECEDENCE.get(c_exp) is None: #if it is an operand
                postfix += c_exp + " "
            else: #if it is not an operand
                if(c_exp != ')'):
                    if(stack.isEmpty() or c_exp == '('):
                        stack.push_back(c_exp)
                    elif PRECEDENCE.get(stack.peek()) < PRECEDENCE.get(c_exp):
                        stack.push_back(c_exp)
                    else: # <=
                        while not stack.isEmpty() and PRECEDENCE.get(stack.peek()) >= PRECEDENCE.get(c_exp):
                            postfix += stack.peek()
                            stack.pop_back()
                        stack.push_back(c_exp)
                else:
                    while(stack.peek() != '('):
                        if (stack.peek() != '('):
                            postfix += stack.peek() + " "
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
        if len(self.expression) == 1:
            return self.value
        stack = Stack()
        index = 0
        while index < len(self.expression):
            c_exp = " "
            while(not index == len(self.expression) and self.expression[index] != " "):
                c_exp += self.expression[index]
                index = index + 1
            index = index + 1
            if PRECEDENCE.get(c_exp[1:]) is None :  # if it is an operand
                stack.push_back(c_exp)
            else:
                operation = c_exp[1:]
                if operation == "^":
                    operation = "**"
                operand2 = stack.peek()
                if self.key == str(operand2):
                    operand2 = self.value
                stack.pop_back()
                operand1 = stack.peek()
                if self.key == str(operand1):
                    operand1 = self.value
                stack.pop_back()
                result = eval(str(operand1)+operation+str(operand2))
                stack.push_back(result)
        return stack.peek()




