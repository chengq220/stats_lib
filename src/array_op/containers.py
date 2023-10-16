class LinkedNode():
    def __init__(self, value=None):
        self.value = value
        self.prev = self
        self.next = self

    def getValue(self):
        if(self.value is None):
            raise Exception("Value did not get initialized")
        return self.value

    @staticmethod
    def linkNode(first, second):
        first.next = second
        second.prev = first

    @staticmethod
    def unlinkNode(node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

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
    def addNodeTail(self, value):
        if(self.isEmpty()):
            self.head = LinkedNode(value)
            self.tail = self.head
        else:
            newNode = LinkedNode(value)
            LinkedNode.linkNode(self.tail, newNode)
            self.tail = newNode
        self.size = self.size + 1

    """
    @brief overloaded add node in between two nodes
    """
    def addNode(self, value, prev, next):
        newNode = LinkedNode(value)
        LinkedNode.linkNode(prev, newNode)
        LinkedNode.linkNode(newNode, next)
        self.size = self.size + 1

    """
    @brief      Return the node at a given index
    @param  n   The index of the desired node
    """
    def getNodeIndex(self, n):
        if(n < 0 or n > self.size):
            raise Exception("Index out of bound")
        if(n == 0):
            return self.head
        elif(n == self.size-1):
            return self.tail
        else:
            ptr = self.head
            for i in range(n):
                ptr = ptr.next
            return ptr

    """
    @brief      Remove the node at a given index
    @param  n   The index of the node to be removed
    """
    def removeNodeIndex(self, n):
        if(n == 0):
            self.head = self.head.next
        elif(n == self.size-1):
            self.tail = self.tail.prev
        else:
            LinkedNode.unlinkNode(self.getNodeIndex(n))


    def isEmpty(self):
        return self.size == 0

    """
    @brief  Override the print method
    """
    def __str__(self):
        returnStr = ""
        current = self.head
        for i in range(self.size):
            returnStr += current.value + " "
            current = current.next
        return returnStr

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

    def pop_back(self):
        if(self.__array == 0):
            raise Exception("Attempting to pop from empty stack")
        self.__array.pop(self.__index-1)
        self.__index = self.__index - 1

    def peek(self):
        if(self.__index == 0):
            raise Exception("Attempting to peek into an empty stack")
        return self.__array[self.__index-1]

# class queue():
#     def __init__(self):
#         self.array
