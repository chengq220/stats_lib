from src.util.parser import parser
from src.calculus.integration import integral_apprx
from src.statistics.distributions import Normal_Distribution

# n = Normal_Distribution(0, 1)
# print(n.cdf(1,2))
p = parser("2.01 * 3")
print(p.getPostOrderExpression())
# print(p.evaluate())