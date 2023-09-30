import matplotlib.pyplot as plt
from .stat_operations import *
from src.array_op.list_operations import *
from src.array_op.sort import *

class Plots:
    @staticmethod
    def qq_plot(array):
        mean = Stat_Op.find_mean(array)
        std = Stat_Op.find_std(array)
        index = List_Op.arange(len(array))
        sorted_arr = Sort.selection_sort(array)
        norm = Stat_Op.normsinv(Stat_Op.get_normal_percentile(index))
        q2 = Plots.generate_q2(norm, std, mean)

        plt.scatter(q2, array, color='blue')
        plt.plot([0, sorted_arr[len(sorted_arr)-1]],
                [0, sorted_arr[len(sorted_arr)-1]], label='y = x', color='red')
        plt.ylabel("Q2")
        plt.xlabel("Imperical Value")
        plt.savefig("plot_test")

    @staticmethod
    def generate_q2(normsinv, std, mean):
        q2 = []
        for i in range(len(normsinv)):
            q2.append((normsinv[i] * std) + mean)
        return q2
