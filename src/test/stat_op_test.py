from stat_operations import *

TOL_CONST = 1e-3

def test_mean():
    arr = [1,1,1,1,1]
    mean = find_mean(arr)
    if(mean < 1 - TOL_CONST or mean > 1 + TOL_CONST):
        print("Test 1.1 failed")
    arr = [1,2,1,2,1,2]
    mean = find_mean(arr)
    if(mean < 1.5 - TOL_CONST or mean > 1.5 + TOL_CONST):
        print("Test 1.2 failed")
    arr = [1,2,3,4,5]
    mean = find_mean(arr)
    if(mean < 3 - TOL_CONST or mean > 3 + TOL_CONST):
        print("Test 1.3 failed")

def test_variance():
    arr = [1,2,3,4,5]
    variance = find_variance(arr)
    if(variance < 2.5-TOL_CONST or variance > 2.5+TOL_CONST):
        print("Test 2.1 failed")
    arr = [1,3,4,5,61,2,3]
    variance = find_variance(arr)
    if(variance < 482.2381-TOL_CONST or variance > 482.2381+TOL_CONST):
        print("Test 2.2 failed")

def test_std():
    arr = [1,2,3,4,5]
    std = find_std(arr)
    if(std < 1.5811388-TOL_CONST or std > 1.5811388+TOL_CONST):
        print("Test 3.1 failed")
    arr = [1,3,4,5,61,2,3]
    std = find_std(arr)
    if(std < 21.95992-TOL_CONST or std > 21.95992+TOL_CONST):
        print("Test 3.2 failed")

def test_normal_percentile():
    arr = get_normal_percentile([0,1,2,3,4])
    ground_truth = [0.1, 0.3, 0.5, 0.7, 0.9]
    for i in range(len(arr)):
        if(arr[i] < ground_truth[i] - TOL_CONST or arr[i] > ground_truth[i] + TOL_CONST):
            print("Test 4.1 failed")
            break

def test_normsinv():
    percentile = [0.1, 0.3, 0.5, 0.7, 0.9]
    result = normsinv(percentile)
    ground_truth = [-1.28155, -0.5244005, 0, 0.5244005, 1.28155]
    for i in range(len(percentile)):
        if(result[i] < ground_truth[i] - TOL_CONST or result[i] > ground_truth[i] + TOL_CONST):
            print("Test 5.1 failed")
            break


if __name__ == "__main__":
    print("testing start")
    test_mean()
    test_variance()
    test_std()
    test_normal_percentile()
    test_normsinv()
