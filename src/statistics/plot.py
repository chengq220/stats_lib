import matplotlib.pyplot as plt
from statistics.array_operations import *
from statistics.stat_operations import *
from src.sorting.sort import *

class plots:
    def qq_plot(self,array):
        mean = find_mean(array)
        std = find_std(array)
        index = arange(len(array))
        sorted_arr = selection_sort(array)
        norm = normsinv(get_normal_percentile(index))
        q2 = generate_q2(norm, std, mean)

        plt.scatter(q2, array, color='blue')
        plt.plot([0, sorted_arr[len(sorted_arr)-1]],
                [0, sorted_arr[len(sorted_arr)-1]], label='y = x', color='red')
        plt.ylabel("Q2")
        plt.xlabel("Imperical Value")
        plt.savefig("plot_test")

    def generate_q2(self, normsinv, std, mean):
        q2 = []
        for i in range(len(normsinv)):
            q2.append((normsinv[i] * std) + mean)
        return q2


if __name__ == "__main__":
    print("testing start")
    p = plots()
    p.qq_plot([25,49,37,64,75])
