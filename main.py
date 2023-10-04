from src.statistics.plot import qq_plot
from src.statistics.distributions import Bernoulli, Binomial_Distribution

b = Binomial_Distribution(10, 0.5)
b.visualize_pmf()
