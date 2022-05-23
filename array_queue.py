
import arrays


#write the snippet that will handle wrapping the last index
#around to 0 if it moves past the end of the array
"""
an_array[last] = value
last+=1
last = last % len(an_array) #len = 10, last = 10, last % len = 0
if last == len(an_array):
    last = 0
"""
#write the code snippet that will determine that the array is full and raise an index error
"""
if size == len(an_array):
    raise IndexError("The array be full, matey.")
"""

class Queue:
    __slots__ = ["__size", "__front", "__back", "__array"]
    def __init__(self, capacity=3):
        self.__array = arrays.Array(capacity, None)
        self.__size = 0
        self.__front = 0
        self.__back = 0
    def size(self):
        return self.__size
    def is_empty(self):
        return self.__size == 0
    def front(self):
        if self.__size == 0:
            raise IndexError("Can't look at front of empty queue.")
        else:
            return self.__array[self.__front]
    def back(self):
        if self.__size == 0:
            raise IndexError("Can't look at back of empty queue.")
        else:
            return self.__array[self.__back - 1]
    def enqueue(self, value):
        if self.__size == len(self.__array):
            self.__resize()
        self.__array[self.__back]
        self.__back += 1
        if self.__back == len(self.__array):
            self.__back = 0
        self.__size+=1
    def dequeue(self):
        if self.__size == 0:
            raise IndexError("Can't dequeue from an empty queue.")
        else:
            value = self.__array[self.__front]
            self.__array[self.__front == None]
            self.__front +=1
            if self.__front == len(self.__array):
                self.__front = 0
            self.__size -=1
            return value
    def __resize(self):
        new_array = arrays.Array((len(self.__array)*2)+1)
        i = self.__front
        j = 0
        for _ in range (self.__size):
            new_array [j] = self.__array[i]
            i = (i +1 ) % len(self.__array)
            j +=1
        self.__front = 0
        self.__back = j
        self.__array = new_array
