import math
from statistics import NormalDist

class Stat_Op():
    @staticmethod
    def find_mean(array, power=1):
        sum = 0
        for i in array:
            sum += (i**power)
        return sum/len(array)

    @staticmethod
    def find_variance(array):
        length = len(array)
        mean = Stat_Op.find_mean(array)
        difference_2 = 0
        for i in array:
            difference_2 += ((i - mean) ** 2)
        return (1/(length-1)) * difference_2

    @staticmethod
    def find_std(array):
        return math.sqrt(Stat_Op.find_variance(array))

    @staticmethod
    def get_normal_percentile(index):
        length = len(index)
        percent = []
        for i in range(len(index)):
            percent.append((i+1 - 0.5)/length)
        return percent

    """
    @param percentile       The percentile of each element in a normal distribution
    """
    @staticmethod
    def normsinv(percentile):
        inv = []
        for i in range(len(percentile)):
            inv.append(NormalDist(mu=0, sigma=1).inv_cdf(percentile[i]))
        return inv
