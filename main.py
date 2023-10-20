from src.util.parser import parser

p = parser('2+(x*1)-y',{'x':3, 'y':9})
print(p.evaluate())

