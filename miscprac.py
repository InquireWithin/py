import arrays
import array_queue
import array_utils
import node_stack
import random
import csv
import turtle
def the_translator(phrase):
    consonant_directory = ("B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","Y","V","X","Z")
    vowel_directory = ("A","E","I","O","U")
    translated = ""
    words = phrase.split()
    for word in words: #take the user input, split it up into individual words, and 
        first = word[0]
        first = str(first)
        first = first.upper() #this is needed simply because the datasets containing the vowels
        #and non-vowels are all uppercase.
        #this was accidental, i was thinking of the names in the streets.csv file, which are in caps, when i was
        #re-do ing this function

    #the first or second letter in every word has to be a vowel, this if and elif will determine the entirety
    #of the pig-latin word based on this fact
    if first in consonant_directory:
        length_of_word = len(word)
        remove_first = word[1:length_of_word] #take the first letter and readd it at the end.
        pig_latin=remove_first + first + "ay"
        translated = translated+ " " +pig_latin
    elif first in vowel_directory:
        pig_latin=word+"ay" #literally just adds "ay" to the word, theres nothing more to do here.
        translated=translated+" "+pig_latin #add it to the blank string, translated.
    translated = translated.strip()
    return translated

def polygon(side_length, sides, color = "green"):
    perimeter = side_length * sides #reminder to use this for testing later
    turn = 360 / sides
    if sides < 3:
        raise ValueError("Number of sides must be 3 or larger.")
    else:
        turtle.up()
        turtle.setpos(0,0)
        turtle.down()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(sides):
            turtle.right(turn)
            turtle.forward(side_length)
        turtle.end_fill()
import csv
def find_streets(filename, street_name):
    total = ""
    try:
        with open(filename) as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file)
            for record in csv_reader:
                
                if record[0] == street_name:
                    total += str(record)
                    
                
            
            return total
    except ValueError:
        print("Street name couldn't be found.")
    except FileNotFoundError:
        print("File couldn't be found.")

def find_popular_street(filename):
    most_popular = ""
    count = 0
    highest_count = 0
    with open(filename) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file)
        for record in csv_reader:
            count = 0
            output = find_streets("data/streets.csv", record[0])
            output = str(output)
            output_split = output.split("[")
            #print("All street names for ", record[0])
            #print(output_split)
            for line in output_split:
                #print("Split Line: ", line)
                count +=1
            if count > highest_count:
                highest_count = count
                most_popular = record[0]

        return most_popular

def drives(filename ="data/streets.csv"):
    #parses the file looking for, and then counting, each street ending in "DR"
    street_set = set()
    count = 0
    with open(filename) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file)
        for record in csv_reader:
            if record[1] == "DR" and record[0] not in street_set:
                    count +=1
                    street_set.add(record[0])
        return count
def find_red_leaf(filename = "data/streets.csv"):
    #parses the streets file checking for if there's a such street as "RED LEAF LN"
    found = False
    with open(filename) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file)
        for record in csv_reader:
            _str = (record[0] + " " + record[1])
            if _str == "RED LEAF LN":
                found = True
            if found is True:
                break
        return found

def vistas(filename = "data/streets.csv"):
    #counts the street types for all streets contaning "VISTA"
    street_set = set()
    with open(filename) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file)
        for record in csv_reader:
            init_record = record[0]
            split_record = init_record.split(" ")
            for i in split_record:
                if i == "VISTA" and record[1] not in street_set:
                    street_set.add(record[1])
        return street_set

class Exam:
    __slots__ = ["__student", "__max_points", "__points"]
    def __init__(self, student, max_points, points):
        self.__student = student
        self.__max_points = max_points
        self.__points = points

    def get_grade(self):
        return 100*(self.__points / self.__max_points)
    def take_exam(self, student_name):
        self.__student = student_name
    def grade_exam(self, points_earned):
        self.__points = points_earned
    def get_student(self):
        return str(self.__student)
    def get_max_points(self):
        return self.__max_points
    def __str__(self):
        grade = self.get_grade
        string_grade = str(grade)
        return (str(self.__student) + string_grade)
    def __eq__(self, other):
        return self.__student == other.__student and \
            self.__points == other.__points and \
            self.__max_points == other.__max_points
    def __hash__(self):
        return hash(self.__student) * self.__max_points * self.__points

def add_exam(exam, turn_in):
    #add an exam to the collection
    turn_in.push(exam)
    return turn_in
def collection(exam_list):
    instructor_stack = node_stack.Stack()
    random.shuffle(exam_list) #<- "randomize" who finishes first, last, and everything in between
    for test in exam_list:
        add_exam(test, instructor_stack)
    return instructor_stack
def grade_all_exams(instructor_stack): #grade every exam in the instructor's stack of tests.
    #nts: use a queue instead of flipping face over
    #exam_queue = array_queue.Queue(30) #create a queue with capacity 30, for 30 student's exams

    graded_stack = node_stack.Stack()
    while not instructor_stack.is_empty():

        to_grade = instructor_stack.pop() #take the exam off the top of the stack
        to_grade.grade_exam(random.randint(0,100)) #grade it
        # exam_queue.enqueue(to_grade) #add it
        graded_stack.push(to_grade)
    return graded_stack #return
def update_repository(repository, graded_stack):
    exam = graded_stack.pop()
    #print("Pushed to stack: exam of student", str(exam.get_student()))
    #print("Points: ", exam.get_grade())
    #print("Max points: ", exam.get_max_points())
    #exam_queue.dequeue()
    repository[str(exam.get_student())] = int(exam.get_grade())
    #print("Repository at student ", exam.get_student(), "is", repository[str(exam.get_student())])
    return graded_stack
def increasing_comparator(a,b):
    return a < b

def decreasing_comparator(a, b):
    return a > b
def swap(an_array, a, b):
    #swap the values at a and b
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp
def shift(an_array, index):
#as long as the value at index is less than the value at index - 1
# -
#AND index is greater than 0, swap
    if index > 0:
        while an_array[index] < an_array[index - 1] and index > 0:
            swap(an_array, index, index-1)
            index +=1
def insertion_sort(an_array):
    #loop over the indexes in an_array starting at index 1
    #call shift
    d = 0
    for index in range(len(an_array)): # <- old function that doesnt use comparator.
        print("d: ", d)
        print("index: ", index)
        if d > 0:
            shift(an_array, index)
            d+=1
        else:
            d+=1
            #continue
def get_lowest(an_array): #custom helper func i made to fix a logic error involving
    #insertion sort
    lowest = 100
    for num in range(an_array):
        if an_array[num] < lowest:
            lowest = an_array[num]
    return num
    
def split(an_array):
    # determine the length of evens and odds
    length = len(an_array)
    odd_length = length // 2
    even_length = length - odd_length

    # create the evens and odds arrays
    evens = arrays.Array(even_length)
    odds = arrays.Array(odd_length)

    # copy all of values at even indexes into evens
    # copy all of the values at odd indexes into odds
    even_index = 0
    odd_index = 0

    for index in range(len(an_array)):
        if index % 2 == 0:
            evens[even_index] = an_array[index]
            even_index += 1
        else:
            odds[odd_index] = an_array[index]
            odd_index += 1

    # return evens, odds
    return evens, odds
def merge(left, right):
    # create an array of left length + right length
    left_length = len(left)
    right_length = len(right)
    merged = arrays.Array(left_length + right_length)

    #keep track of 3 indexes: merged, left, right
    left_index = 0
    right_index = 0
    #merged_index = 0
    #loop until we've copied everything from left and right
    while left_index < left_length and right_index < right_length:

        #compare values at left index and right index
        if left[left_index] < right[right_index]:
            #copy from left to merged
            merged[left_index + right_index] = left[left_index]
            left_index +=1
        else:
            #copy from right to merged
            merged[left_index + right_index] = right[right_index]
            right_index+=1
        
        
       
    #copy remaining elements from other array (left or right)
    if left_index < left_length:
        #stuff left in left
        #while(left_index < left_length): # can be done w/ while or for loop
        for index in range(left_index, left_length):

            merged[index + right_index] = left[index]
    elif right_index < right_length:
        #stuff left in right
        for index in range(right_index, right_length): # can be done with for or while loop
            merged[index + left_index] = right[index]
            
    #return merged
    return merged

def merge_sort(an_array):
    if len(an_array) == 0:
        return an_array
    elif len(an_array) == 1:
        return an_array
    else:
        left, right = split(an_array)

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        merged = merge(merge_sort(sorted_left), merge_sort(sorted_right))

        return merged
def sort_repository(repository):
    grade_array = arrays.Array(30)
    #print("Repo before sort: ", repository)
    for a in range(len(grade_array)): #for each grade in the dictionary/grade repo:
        grade_array[a] = repository[str(a)]
    merge_sort(grade_array)
    #print("Sorted grades: ", grade_array)
    for b in range(len(grade_array)):
        repository[str(b)] = grade_array[b]
    
    #print("Repository: ", repository)    
    return repository
    
def is_power(x,y):
    #return true if x is a power of y

    if x == 1 or x%y == 0:
        return True
    else:
        return False

def what_power(x,y, count = 0):

    if x == 1:
        return 0
    elif x%y == 0:
        count = what_power(x%y, y)
        return count+1
    else:
        raise ValueError("x is not a power of y")

def range_array(an_array, start = 0, step = 1, index = 0):
    #base case: stop when array is full

    #how do you know when the array is full? this is usually done
    #by comparing something to the length of an_array
    

    #fill the array with values in the range using recursion
    if index == len(an_array):
        pass
    else:
        an_array[index] = start
        range_array(an_array, start + step, step,index+1)
def range_array_2(an_array, start = 0, step = 1):
    pass
def arrays_equal(a_array, b_array):
    #return true if both arrays contain all of the same elements
    #false otherwise
    if len(a_array) > len(b_array) or len(a_array) < len(b_array):
        return False
    else:
        for i in range(len(a_array)):
            if a_array[i] == b_array[i]:
                continue
            else:
                return False
        return True



"""
Time complexities of: [best, worst, expected]
Linear Search [best: o(1), worst: o(n), expected: o(n)]
Binary Search [o(1) or o(c), o(logn), o(logn) ]
insertion sort [o(n), o(n^2), o(n^2)
bubble sort o(n), o(n^2), o(n^2)
merge sort o(nlogn), o(nlogn), o(nlogn)
quicksort o(nlogn), o(n^2), o(n^2)
binary sort: doesn't exist
"""

#tuples and lists unit
#tuples
def tuplify():
    #prompt user to enter first middle and last name
    #return it as a tuple
    #if middle name is an emoty string dont include it

    first = input ("Enter first name: ")
    middle = input("Enter middle name: ")
    last = input("Enter last name: ")
    if middle == "":
        a_tuple = (first, last)
        return a_tuple
    else:
        a_tuple = tuple(first, middle, last)
        return a_tuple
#lists
def cubed(a_list):
    for i in range(len(a_list)):
        trip = a_list[i] ** 3
        a_list[i] = trip
    return a_list
#list in reverse order, linear time
def reversal(a_list):
    reversed_list = []
    index_length = len(a_list) - 1
    for i in range(len(a_list)):
        reversed_list.append(a_list[index_length - i])
    return reversed_list

#multiplication table. 2d list/2d arrays

def multiples(rows, cols):
    table = [[]]
    #a = 1
    #b = 1
    for a in range(rows):
        table_row = []
        for b in range(cols):
            product = (a+1) * (b + 1)
            
            table_row.append("{: >2d}".format(product))
        table.append(table_row)
    return table

#pytest
#capsys and monkeypatch?

"""
#data type, access/update, insert/delete, orderable?, elements unique?
Array, o(c), o(n), yes, no
List, o(c), o(n), yes, no
Dict, o(c), o(c), (no for python <3.6, yes for python >3.7), (Keys = yes, values = no)
Set, o(c), o(c), no, Yes
Stack, o(c), o(c), Yes, no
Queue, o(c), o(c), yes, no
"""

def main():
    #_s = "have you ever heard the tragedy of darth plagueis the wise"  
    #print(_s.split())
    #word = "moyai"
    #pig_latin_translator(word)
    #print(the_translator("moyai"))
    #polygon(100, 3)
    #input("yoink")
    #print(find_streets("data/streets.csv", "FIRST"))


    #popular = find_popular_street("data/streets.csv")
    #print(popular)
    """
    #print(drives())
    #print(find_red_leaf())
    #print(vistas())
    #There are 150 DR's, excluding post directions

    #exam list
    exam_list = []
    #create 30 students to take an exam
    i = 0
    while i < 30:
        exam = Exam(i, 100, 0)
        exam_list.append(exam)
        i+=1
    #when students are done with the exam, turn it in, they will be organized into the
    #instructor stack
    instructor_stack = collection(exam_list)
    #exams will now be taken off the instructor stack and graded
    graded_stack = grade_all_exams(instructor_stack)
    #enter the grades int the grade repository
    #create a grade repo:
    repository = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,
    "15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"21":0,"22":0,"23":0,"24":0,"25":0,"26":0,"27":0,"28":0,"29":0}
    while not graded_stack.is_empty():
        graded_stack = update_repository(repository, graded_stack)
        #print("Current repostiory", repository)
        #print("Current graded stack: ", graded_stack)
    #sirt the repository by the grades
    repository = sort_repository(repository)
    print(repository)
    """
    # x = 9
    # y = 81
    # print(is_power(x,y))

    # c_array = arrays.Array(11)
    # a_array = arrays.Array(10)
    # b_array = arrays.Array(10)
    # print(arrays_equal(a_array, c_array))

    # a_list = [5,3,7,2,1]
    # print(reversal(a_list))

    #print(multiples(5,5))
    pass
if __name__ == "__main__":
    main()

