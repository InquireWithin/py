from _node import *

class Queue:
    __slots__ = ["__front", "__back", "__size"]
    def __init__(self):
        self.__front = None
        self.__back = None
        self.__size = 0
    def get_size(self):
        return self.__size
    def set_size(self, value):
        self.__size = value
        
    #when the size is 0 and you enqueue, you need to set both front and back to the new Node.

    #when the size is 1 and you dequeue, you need to set the front and back both to None.
    """
    def enqueue(self, value):
        if self.__size == 0:
            self.__front = node.get_next()
            self.__back = node.get_next()
        else:
            node.set_next(value)
            self.__back +=1
    """
    def enqueue(self, value):# add a value to the queue
        new_value = Node(value)
        if self.__front is None:
            self.__front = new_value
            self.__back = self.__front
            self.__size +=1
        else:
            self.__front = value
            self.__back.set_next(new_value)
            self.__back = new_value
            self.__size +=1
    def dequeue(self): #remove the most recently queued value
        if self.__size > 0:
            value = self.__front
            _value = Node(value)
            self.__front = _value.get_next()
            self.__size -=1
            if self.__front is None:
                self.__back is None
            return value
        else:
            raise AttributeError("can't dequeue from empty queue.")
    def is_empty(self):
        if self.__size == 0:
            return True
        if self.__front == 0:
            return True
        if self.__back == 0:
            return True
        else:
            return False
        #return self.__back == None
    def front(self): #get the value at the front
        return self.__front.get_value()
    def back(self): #get the value at the back
        return self.__back.get_value()

    def __repr__(self):
        if self.__size == 0:
            return "[]"
        else:
            string = "["
            node = self.__front
            while node is not None:
                string += node.get_value()
                string += ", "
                node = node.get_next()
            string = string + "]"
            return string

def main():
    #setup
    #queue = Queue()
    #invoke
    
    #queue.enqueue(123)
    #analyze
    #print(queue.get_size())
    #print(queue.is_empty())
    #print(queue.front())
    pass
if __name__ == "__main__":
    main()