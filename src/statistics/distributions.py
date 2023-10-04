from math import comb
import matplotlib.pyplot as plt
from src.array_op.list_operations import arange

class Bernoulli():
    def __init__(self, p):
        self.p = p
        self.mean = p
        self.variance = p * (1 - p)

    def pmf(self, x):
        if(x == 1):
            return self.p
        elif(x == 0):
            return 1-self.p
        else:
            raise Exception("Unrecognized value")

    """
    @brief   Create a graph of the bernoulli distribution
    """
    def visualize_pmdf(self):
        outcomes = [0, 1]
        probabilities = [1 - self.p, self.p]
        plt.bar(outcomes, probabilities, tick_label=outcomes)
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.title('Bernoulli Distribution PMF')
        plt.savefig("bernoulli")




class Binomial_Distribution():
    def __init__(self, n, p):
        self.p = p
        self.n = n
        self.mean = n * p
        self.variance = n * p * (1 - p)

    def pmf(self, x):
        if(x > self.n or x < 0):
            return 0
        else:
            return comb(self.n,x) * self.p ** x * (1-self.p) ** (self.n-x)

    def visualize_pmf(self):
        outcomes = arange(self.n + 1)
        probabilities = []
        for i in range(self.n+1):
            prob = self.pmf(i)
            probabilities.append(prob)
        plt.bar(outcomes, probabilities, tick_label=outcomes)
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.title('Binomial Distribution PMF')
        plt.savefig("binomial")

    """
    @brief   Calculate the probability of p(x1 <= X <= x2)
    """
    def cdf(self, x1, x2):
        prob = 0
        if(x1 == x2):
            prob = prob + self.pmf(x1)
        else:
            prob_l = 0
            for i in range(0, x2+1):
                pmf = self.pmf(i)
                prob = prob + pmf
                if(i <= x1):
                    prob_l = prob_l + pmf
            prob = prob - prob_l
        return prob

    def visualize_cdf(self):
        outcomes = arange(self.n + 1)
        probabilities = []
        prob = 0
        for i in range(self.n+1):
            prob = prob + self.pmf(i)
            probabilities.append(prob)
        plt.bar(outcomes, probabilities, tick_label=outcomes)
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.title('Binomial Distribution CDF')
        plt.savefig("binomial")
#
#     class multinomial_distribution():
#         """
#         @param prob_arr  the array containing the probability of the different
#                          outcomes
#         """
#         def __init__(self, prob_arr):
#             self.p = prob_arr
#
#         """
#         @param bum_obj   the array containing the occurences of the different
#                          outcomes
#         """
#         def pmf(self, num_obj):
#             if(len(num_obj) != len(prob_arr)):
#                 raise Exception("Probability array size does not match")
#             else:
#                 prob = 0
#
#
#         def cdf(self,x1, x2=x1):
#             prob = 0
#             if(x1 == x2):
#                 for i in range(0, x1+1):
#                     prob = prob + self.pmf(i)
#             else:
#                 prob_l = 0
#                 for i in range(0, x2+1):
#                     pmf = self.pmf(i)
#                     prob = prob + pmf
#                     if(i <= x1):
#                         prob_l = prob_l + pmf
#                 prob = prob - prob_l
#             return prob

        # def visualize(self):
