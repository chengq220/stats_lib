from src.util.parser import parser
from src.calculus.integration import integral_apprx
from src.statistics.distributions import Normal_Distribution
#
# n = Normal_Distribution(10, 4)
# print(n.cdf(1,6))
# p = parser("(1/(5*2))*3^(20/8*x-x^2-100/8)", 'x', 2)
p = parser("( 210 * 250 ) - 4 ")
print(p.getPostOrderExpression())
print(p.evaluate())
# print(p.evaluate())