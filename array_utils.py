import arrays
import random



def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array

def random_array(size, min_value=0, max_value=None):
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size

    for index in range(size):
        an_array[index] = random.randint(min_value, max_value)
    
    return an_array

def main():
    # numbers = range_array(1, 21)
    # print(numbers)
    # odds = range_array(1, 12, 2)
    # print(odds)
    # evens = range_array(0, 11, 2)
    # print(evens)
    # backwards = range_array(10, -1, -1)
    # print(backwards)
    # negatory = range_array(-1, -10, -1)
    # print(negatory)

    random.seed(1)
    rand_array = random_array(10)
    print(rand_array)


if __name__ == "__main__":
    main()