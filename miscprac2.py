#c:\Users\optimus\primes.txt
#c:\users\optimus\hello.py
#c:\users

#cd users\optimus
#cd ..
#ls c:\Program Files
#notepad info.txt
#rm hello.py
#
#
#w
import math
import turtle

def mathematics():
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a valuefor y: "))
    print("x^y: ", x**y)
    
def distance(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def triangle(x1,y1,x2,y2,x3,y3, color="red"):
    turtle.speed(5)
    turtle.up()
    turtle.setpos(x1,y1)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setpos(x2,y2)
    turtle.setpos(x3,y3)
    turtle.setpos(x1,y1)
    turtle.end_fill()
    turtle.up()
    side1 = distance(x1,y1,x2,y2)
    side2 = distance(x2,y2,x3,y3)
    side3 = distance(x1,y1,x3,y3)
    return side1+side2+side3

def chop_chop(a_string):
    index = 0
    chopped = ""
    while index <len (a_string):
        chopped += a_string[index]
        index+=2
    while index < len(a_string):
        chopped += a_string[index]
        index +=2
    return chopped
def unchop(a_string):
    length = len(a_string)
    original = ""
    #adds to original 2 at a time
    for even_index in range(0, length - length //2):
        original += a_string[even_index]
        odd_index = (length - length //2 ) + even_index
        if odd_index < length:
            original += a_string[odd_index]
    return original
    
#unit 5
import csv
def starts_with(filename, letter):
    count = 0
    with open(filename) as file:
        for line in file:
            for word in line:
                if word[0] == letter:
                    count+=1

    return count
def zip_lookup(filename, zip_code):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for record in csv_reader:
            if record[0] == zip_code:
                return record[1]
        raise ValueError("Bad zip code: ", zip_code)
def main():
    pass
    print("name")
    print("class")
    print(starts_with("data/atotc.txt", "a"))
    while True:
        try:
            zip_code = input("Enter zip code: ")
            location = zip_lookup("data/zip_codes.csv", zip_code)
            print(location)
        except FileNotFoundError:
            print("bad zip code file")
            break

        except ValueError:
            print("zip code not found.")
    print("Goodbye!")
if __name__ == "__main__":
    main()