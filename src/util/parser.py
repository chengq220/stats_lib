"""
@brief    Parser for mathematical equations that uses postfix stack implementation
"""
class parser:
    def __init__(self, string, vars={}):
        self.expression = string
        self.index = 0
