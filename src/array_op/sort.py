
"""
@brief          A simple implementation of the selection sort algorithm
@param array    The array to be sorted
@return         A sorted array
"""
def selection_sort(array):
    new_array = array
    for i in range(len(new_array)):
        low_idx = i
        for j in range(i+1,len(new_array)):
            if new_array[j] < new_array[low_idx]:
                low_idx = j
        temp = new_array[i]
        new_array[i] = new_array[low_idx]
        new_array[low_idx] = temp
    return new_array
