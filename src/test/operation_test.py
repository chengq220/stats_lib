from array_operations import *

def test_arange():
    list = arange(1)
    if(list[0] != 0 or len(list) != 1):
        print("Test 1.1 failed")
    list = arange(5)
    for i in range(len(list)):
        if(list[i] != i):
            print("Test 1.2 failed")
            break
    if(len(list) != 5):
        print("Test 1.2 failed")
    list = arange(10)
    for i in range(len(list)):
        if(list[i] != i):
            print("Test 1.2 failed")
            break
    if(len(list) != 10):
        print("Test 1.3 failed")

if __name__ == "__main__":
    print("testing start")
    test_arange()
