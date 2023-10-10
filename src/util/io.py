import csv

"""
@brief           Expect to take in a csv file containing integer
@param read_dir  Path to the csv file
@return          A python list containing all the values stored in the csv
"""
def read_file(read_dir, delim = ","):
    r = []
    with open(read_dir, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim)
        for row in reader:
            r.append(row)
    return r


"""
@brief           Write to an array to csv
@param array     Information to write to file
@param file_dir  Path to store the new csv file
"""
# def write_file(array, file_dir):
#     # TODO:
