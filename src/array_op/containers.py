class LinkedNode():
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

    def getValue():
        if(value is None):
            raise Exception("Value did not get initialized")
        return self.value

    @static
    def linkNode(first, second):
        first.next = second
        second.prev = first

"""
@brief A doubly linked list
"""
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    """
    @brief Add the node to the end of the linked list
    """
    def addNode(self, value):
        if(self.head is None):
            self.head = LinkedNode(value)
            self.tail = self.head
        else:
            newNode = LinkedNode(value)
            linkNode(self.tail, newNode)
            self.tail = newNode
        self.size = self.size + 1

    """
    @brief overloaded add node in between two nodes
    """
    def addNode(self, value, prev, next):
        newNode = LinkedNode(value)
        linkNode(prev, newNode)
        linkNode(newNode, next)

    def getIndex(self, n):
        if(n < 0 or n > self.size):
            raise Exception("Index out of bound")
        if(n == 0):
            return self.head.value;
        else if(n == self.size-1):
            return self.tail.value
        else:
            ptr = self.head
            for i in range(n):
                ptr = self.head.next
            return ptr.value



"""
@brief A stack implementation using arrays
"""
class Stack():
    def __init__(self):
        self.__array = []
        self.__index = 0

    def push_back(self, item):
        self.__array.append(item)
        self.__index = self.__index + 1

    def pop_back(self, item):
        if(self.index == 0):
            raise Exception("Attempting to pop from empty stack")
        self.__array.pop(self.__index)
        self.__index = self.__index - 1

    def peek(self):
        if(self.index == 0):
            raise Exception("Attempting to peek into an empty stack")
        return array[self.__index]

# class queue():
#     def __init__(self):
#         self.array
