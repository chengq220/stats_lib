from src.util.parser import parser

p = parser('a+b*c-(d/e+f*g*h)')
answer = "abc*+de/fg*h*+-"
print(p.getExpression() == answer)

