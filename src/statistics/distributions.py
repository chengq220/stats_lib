import math
from math import comb, factorial, e
import matplotlib.pyplot as plt
from src.array_op.list_operations import arange
from src.calculus.integration import integral_apprx

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

class Normal_Distribution():
    def __init__(self, mean, variance):
        self.mean = mean
        self.variance = variance
        self.__upper = int(mean + 3 * variance ** (1/2))
        self.__lower = int(mean - 3 * variance ** (1/2))

    """
    @brief  Crude Approximation of the cdf between two bounds
            P(x1 < x < x2)
    """
    def cdf(self, x1, x2):
        coeff = int(math.sqrt(2 * math.pi * self.variance))
        euler_coef = int(2.7182818)
        denom = int(2.0 * self.variance)
        tm = int(2.0 * self.mean)
        m_2 = int((self.mean * 1.0) ** 2)
        func = "(1/(" + str(coeff) + "*" + str(euler_coef) + "))" + "^(" + str(tm) + "/" + str(denom) + "*x-x^2-" + \
               str(m_2) + "/" + str(denom) + ")"
        return integral_apprx(func, x1, x2, 'x')
