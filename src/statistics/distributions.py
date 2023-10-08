from math import comb, factorial, e
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


class Multinomial_Distribution():
    """
    @param prob_arr  the array containing the probability of the different
                     outcomes
    @param n         number of items to choose from
    """
    def __init__(self, n, prob_arr):
        if(self.__sum_probability(prob_arr)):
            self.p = prob_arr
        self.n = n

    """
    @param bum_obj   the array containing the occurences of the different
                     outcomes
    """
    def pmf(self, num_obj):
        sum = 0
        for i in num_obj:
            sum = sum + i
        if(len(num_obj) != len(self.p)):
            raise Exception("Size mismatch")
        elif(sum != self.n):
            raise Exception("The array does not add up to n")
        else:
            n = 0
            for i in num_obj:
                n = n + i
            prob = factorial(n)
            for i in num_obj: #n^2 since factorial is O(n)
                prob = prob/factorial(i)
            for i in range(len(num_obj)):
                prob = prob * (self.p[i] ** num_obj[i])
            return prob
    """
    @brief  check if the probability array provided adds up to 1
    """
    def __sum_probability(self, prob_arr):
        prob = 0
        for i in prob_arr:
            prob = prob + i
        if(prob != 1):
            raise Exception("The probability does not add up to 1")
        return True


class Poisson_Distribution():
    def __init__(self, lbda):
        self.lbda = lbda
        self.mean = lbda
        self.variance = lbda

    def pmf(self, x):
        if(type(x) is not int):
            raise Exception("Parameter have to be integer value")
        else:
            return (e**(-1 * self.lbda) *
                    self.lbda ** x)/factorial(x)
    """
    @param  n  te upper bound for the number of occurences
    """
    def visualize_pmf(self, n):
        outcomes = arange(n)
        probabilities = []
        for i in range(n):
            prob = self.pmf(i)
            probabilities.append(prob)
        print(probabilities)
        plt.bar(outcomes, probabilities, tick_label=outcomes)
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.title('Poisson Distribution PMF')
        plt.savefig("poisson")

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

    """
    @param  n  te upper bound for the number of occurences
    """
    def visualize_cdf(self, n):
        outcomes = arange(n)
        probabilities = []
        prob = 0
        for i in range(n):
            prob = prob + self.pmf(i)
            probabilities.append(prob)
        plt.bar(outcomes, probabilities, tick_label=outcomes)
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.title('Poisson Distribution CDF')
        plt.savefig("poisson")
