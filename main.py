from src.util.parser import parser

p = parser('a+b*c-(d/e+f*g*h)')
print(p.getExpression())
answer = "abc*+de/fg*h*+-"
print(answer)
print(p.getExpression() == answer)

