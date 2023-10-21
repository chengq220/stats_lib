from sort import *

def test_selection():
    arr = [1,2,3,4,5]
    sorted = selection_sort(arr)
    for i in range(len(arr)):
        if(arr[i] != sorted[i]):
            print("Test 1.1 failed")
            break
    arr = [2,1,5,4,6]
    sorted = selection_sort(arr)
    ground_truth = [1,2,4,5,6]
    for i in range(len(arr)):
        if(sorted[i] != ground_truth[i]):
            print("Test 1.2 failed")
            break
    arr = [6,5,4,3,2,1]
    sorted = selection_sort(arr)
    ground_truth = [1,2,3,4,5,6]
    for i in range(len(arr)):
        if(sorted[i] != ground_truth[i]):
            print("Test 1.3 failed")
            break

if __name__ == "__main__":
    print("testing start")
    test_selection()
