from src.util.parser import parser
from src.calculus.integration import integral_apprx

approx = integral_apprx("x^2", 3, 10, 'x')
print(approx)