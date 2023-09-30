
#returns list of increment by starting at 0 to n-1
class List_Op():
    @staticmethod
    def arange(n):
        list = []
        for i in range(n):
            list.append(i)
        return list
