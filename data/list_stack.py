class Stack:
    __slots__ = ["__list", "__size"]
    def __init__(self):
        self.__list = [] 
        self.__size = 0
    def pull(self):
        return self.__list.pop(len(self.__list)-1)
    def push(self, value):
        self.__list.append(value)
    def peek(self):
        return self.__list[len(self.__list)-1]
    #def __len__
    def get_list(self):
        return self.__list
    def append_list(self, value):
        self.__list.append(value)
    def set_list_indices(self, index, value):
        self.__list.insert(index, value)
    def pop_list(self): #index = len(self.__list) -1):
        self.__list.pop()
    def is_empty(self):
        if self.__list.__len__ == 0:
            return True
        else:
            return False
    def __repr__(self):
        return repr(self.__list)
        
        