import node
#define a stack class with slots for top and size
#methods to check if the stack is empty and get the size
class Stack:
    __slots__ = ["__top", "__size"]
    def __init__(self):
        self.__top = None
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__top is None
    
    def __stringify__(self, node):
        if node is None:
            return ""
        else:
            rest = self.__stringify__(node.get_next())
            if rest == "":
                return str(node.get_value())
            else:
                return rest + ", " + str(node.get_value())
    def __repr__(self):
        #['a', 'b', 'c'] where c is the top of the stack
        return "[" + self.__stringify__(self.__top) + "]"

    def push(self, value):
        #create a new top node with the old top node as its next
        new_top = node.Node(value, self.__top)

        #change the stack's top to the new top
        self.__top = new_top
        #increment the size

        self.__size +=1
    def peek(self):
        #if the stack is empty raise valueerror
        #otherwise return the value at the top
        #in doing so, the value at the top is not removed

        if self.is_empty():
            raise ValueError("Can't peek an empty stack.")
        else:
            return self.__top.get_value()
    def pop(self):
        #if the stack is empty, raise valueerror
        #otherwise save the top value in a variable
        #set the top to top's next node
        #decrement size
        #return the old top value
        if self.is_empty():
            raise ValueError("Can't pop off an empty stack.")
        top_value = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -=1
        return top_value



    