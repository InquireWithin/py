from _node import *
from node_stack import *
from array_queue import *
import csv
import random

#Holy hell. With the sheer magnitude of code thats unoptimized in this file, 
#I could use it as a resume for a job at Valve.


    #I should also mention that ive tried working on this for over 12 hours, and from what i can tell there are 3
    #different bugs that keep swapping between eachother whenever i "patch" one of the others. These are all ocurring
    #inside of the core function in the ship class.

    #these are:
    #can't dequeue from an empty queue (cafeteria queue)
    #can't remove from an empty stack
    #Not shuffling through the crewmates in the cafeteria properly, cafeteria is treated as a stack
    #for some reason. This is evidenced by the fact that the last crewmate added to the cafeteria is
    #the first out. 

    #The cafeteria queue issue could be a result of me not utilizing nodes. But I also don't feel
    #as though my array_queue file works as intended

    #I also think that the initial crewmate at the top of the "queue" (which should be a queue but acts like a 
    # stack) takes place of the rest of the crewmates for unknown reasons.
class Task:
# class responsible for managing the different tasks each crewwmate will have
    __slots__ = ["__name", "__location"]

    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def get_location(self):
        return self.__location

    def __str__(self): #compacted string of what action a crewmmate has to do in a specified location
        return self.__name + " in " + self.__location
    def do_string(self): #a weird accessor method made with the intent of turning a task from the file 
        #into a compact string
        return self.__str__
    #accessors and mutators
    def get_task_name(self):
        return self.__name
    def get_task_location(self):
        return self.__location
    def set_task_name(self, _name):
        self.__name = _name
    def set_task_location(self, _location):
        self.__location = _location
# afunction made outsidde of the task class: Its purpose is to read a set of tasks from a file and
# organize them into a collection  
def tasks(filename):
    collection = Stack() #the collection will start off as an empty Stack(). This will rely on
    #nodes and recursion, possibly
    with open(filename) as task_file:
        for line in task_file: #read the file and do the below actions for every line inside the file
            
            line = line.strip()
            line = line.split(",")
            name = line[0]
            location = line[1] #split the lines into 2 different parts to distinguish them
            #between line and location
            task = Task(name, location) #use the task class so we can access its methods
            collection.push(task.do_string()) #add the task's compacted string to the collection stack
    return collection
class Crewmate:
    #class responsible for managing each crewmate, their tasks, status, and visual distinction
    __slots__ = ["__color", "__tasks", "__is_dead"]
    def __init__(self):
        self.__color = None
        self.__tasks = Stack()
        self.__is_dead = False

    def __str__(self):
        #compacted string but formatted based on crewmate's status
        if self.__is_dead == False:
            return self.__color + "Crewmate"
        else:
            return self.__color + "Crewmate [DEAD]"
    def get_dead(self):
        return self.__is_dead
    def set_dead(self, _bool):
        self.__is_dead = _bool
    def assign_task(self, task):
        self.__tasks.push(task)
    def next_task(self):
        return self.__tasks.pop()
    def get_tasks(self):
        return self.__tasks
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
    #use repr to return a more complex string detailing each thing the class is responsible for
    def __repr__(self):
        string = self.__str__ \
            + "\n color = ", self.__color \
            + "\n murdered = ", self.__is_dead \
            + "\n tasks: ", self.__tasks
        return string

def imposter_func(): #helper function for setting the starting number of imposters in the game
    num_imposters = input("How many imposters would you like among us? ")
    num_imposters = int(num_imposters)
    if num_imposters == 1 or 2 or 3 or 4:
        #self.__imposters = int(num_imposters)
        pass
    else:
        imposter_func()
        raise ValueError("Invalid value set for number of imposters, use an integer between 1 and 4.")
    return num_imposters
            
class Ship:
#possibly use methods from Task class to help with the tasks in spaceship
    __slots__ = ["__tasks", "__locations", "__imposters"]
    def __init__(self):
        self.__tasks = []
        self.__locations = set()
        self.__imposters = []

        #for task in tasks:
            #location = task.get_task_location()
            #self.__locations.add(location) 
        #I think this has been taken care of later down the line
    def get_imposters(self):
        return self.__imposters
    def set_imposters(self, num):
        self.__imposters = num
#num imposters used to be here ->
    def assign_colors(self): #assigns colors to crewmates
        taken_colors = set() #tracks the colors already taken
        i = 0 #used to count the amount of crewmates that have been assigned a color
        #the possible colors each player can have:
        crew_colors = ["Black", "Blue", "Brown", "Cyan", "Green", "Pink", "Purple", "Red", "White", "Yellow"]
        random_crew_colors = [] #this will become a randomized version of the crew color list
        #there will always be 10 people, so it is safe to make a dictionary accounting for all 10 people
        #color_dict = {"person1":"", "person2":"","person3":"","person4":"","person5":"","person6":"","person7":"",
        #"person8":"","person9":"","person10":""}
        while i < 10: # a loop designed to shuffle and filter colors and randomize them, and append
            #them to the random crew color list
            random_int = random.randint(0, 9 - i)

            if crew_colors[random_int] in taken_colors:
                random_int = random.randint(0,9 - i)
                while crew_colors[random_int] in taken_colors: #as long as the calculated color
                    #is found within the taken_colors set, continue searching until
                    #an unassigned color is found
                    random_int = random.randint(0, 9 - i)
            #color_dict[i].append(crew_colors[random_int - 1])
            taken_colors.add(crew_colors[random_int])
            random_crew_colors.append(crew_colors[random_int])
            crew_colors.remove(crew_colors[random_int])
            i+=1
        return random_crew_colors #retrieve the randomized color list
        #notes to self regarding this function:
        #check to see if the dictionary is even needed anymore, or has any application elsewhere
        #crew colors and random crew colors maybe the only things needed, maybe just make
        #random crew colors a set all on its own, or utilize another set
    def assign_tasks(self, playerlist, filename): #funnily enough, this function also must decide who the imposters are
        #as, in this game model, the imposters are given no tasks.
        imposter_set = set() #indexes of the playerlist who are imposters
        line_count = 0
        file_list = []
        crewmates_only = []
        with open(filename) as file:
            for line in file:
                line_count +=1
                file_list.append(line)
        i = 0
        num_imposters = imposter_func()
        while i < int(num_imposters):
            index = random.randint(0,9) 
            while index in imposter_set:
                index = random.randint(0,9) #keep going till a value is returned that isnt already in the imposter set
            imposter_set.add(index)
            self.__imposters.append(playerlist[index])
            i+=1
        for a in range(len(playerlist)): #or use in range 10
            if a in imposter_set: #if the algorithm lands on an index representing an imposter player, continue
                continue
            #therefore, no tasks should ever be added to the imposters, right?
            #i guess not mate because shits still busted
            else:
                collection = Stack()
                num_tasks = random.randint(3,6) #each crewmate will get 3-6 tasks
                for _ in range(num_tasks):
                    
                    line = file_list[random.randint(0, line_count - 1)]
                    line = line.strip()
                    line = line.split(",")
                    name = line[0]
                    location = line[1] #split the lines into 2 different parts to distinguish them
                    self.__locations.add(location) 
                    
                    task = Task(name, location) #use the task class so we can access its methods
                    collection.push(task.__str__()) #add the task's compacted string to the collection stack
                    playerlist[a].assign_task(task.__str__()) #add the task to the player's tasks.
                    #print(task.__str__())
                    self.__tasks.append(task.__str__()) #if i must use this later, distribute at random
                    # 3-6 tasks from each list to a crewmate, or use the randint var again later to distribute
                    # the tasks to each crewmate
                    #this can also be used to determine when every task from every crewmate is complete
        #CONVERT PLAYERLIST TO CREWMATE ONLY LIST
        crewmates_only = []
        for d in range(len(playerlist)):
            if d in imposter_set:
                continue
            else:
                crewmates_only.append(playerlist[d])
        return crewmates_only
    #cafeteria function: manages who leaves and enters the cafeteria, also initializes it at the start

    #Another note, the list that is put in should be the CREWMATE list, no imposters should be inside the cafeteria.
    #Only in a Hi-Rez or Pearl Abyss game would something like this be overlooked.
    def core(self, crewmate_list): #this needs a fix in regards to how it approaches tracking crew
        #tasks, and tasks completed.
        cafeteria = Queue()
        surviving_list = []
        dead_list = []
        list_locations = list(self.__locations)
        for crewmate in crewmate_list: #this is the initialization, could possibly be in a different function
            #or in journey, but not inside of a function.

            cafeteria.enqueue(crewmate)
            print("Loading crewmate ", crewmate, "inside of the cafeteria.")
            print("crewmate has color", crewmate.get_color())
        
        while True:
            #----------
            #errors/bugs:
            #cnt pop off empty stack
            #cant remove from empty queue
            #Causes:
            #results because of cafeteria being treated like a stack instead of a queue
            #second cause: a crewmate has survived and their tasks have run out
            #third cause: dead crewmate attempts to do a task
            #other errors: 
            #refusal for crewmate list to keep track of crewmates
            #actions since last commit:
            #commented out bottom survival if statement
            #commented crew mate list removal on top if statement 
            #changed top if statement's conditions
            #string formatting regarding cafeteria, added cafeteria print
            #next:
            #added a print for the crewmate list in the first survival if statement
            #commented out else continue in the for # of impostors loop
            #changed elif to if for the last if statement in the while loop
            #***got an error resulting from an empty queue here***
            #added if cafeteria is not none on 236
            #added crewmate print statement, commented out the cafeteria on
            #-------------
            print("[Crewmates] The crewmates still in the cafteria are: ")
            for each in crewmate_list:
                print(each, end ="", sep=" ,")
            print()
            print("[Crewmate] about to be dequeued: ", crewmate)
            if cafeteria is not None:
                cafeteria.dequeue() #crewmate leaves to do their task
            print("[Crewmate] has left the cafeteria: ", crewmate)
            #if crewmate.get_tasks() == None or crewmate.next_task() == None:
            if crewmate.get_tasks().is_empty() and crewmate.get_dead() == False:
                surviving_list.append(crewmate)
                #print(crewmate_list)
                #crewmate_list.remove(crewmate)
            else:
                #if not crewmate.get_tasks().is_empty():
                do_task = crewmate.next_task()
                print(crewmate, "'s |task|: ", do_task) #this is the task that is popped off of the task stack
                do_task = do_task.split(" in ")
                current_task = Task(do_task[0], do_task[1])
                #crewmate is equivalent of player1 or player2 or player3, etc.
                for _ in self.__imposters:
                    imposter_location = list_locations[random.randint(0, len(list_locations) - 1)]
                    print("An <imposter> has been found in", imposter_location)
                    if imposter_location == current_task.get_location():
                        print("[Crewmate]", crewmate, "has been slain by an <imposter> in: ", current_task.get_location())
                        crewmate.set_dead(True) #crewmate is dead
                        #for _ in crewmate.get_tasks(): #a very, very messy way to try to remove tasks
                        #this was my attempted fix
                        while crewmate.get_tasks().is_empty() is not True:
                            
                            removed_task = crewmate.next_task()
                            self.__tasks.remove(removed_task)
                            print("Since [crewmate]", crewmate, "is dead, |task|", removed_task, "has been removed.")
                        dead_list.append(crewmate)
                        crewmate_list.remove(crewmate)
                        print("(Game): Removed [crewmate]", crewmate)
                        print("(Game): Continuing the game...")
                        break #crewmate is already dead, no need to iterate over the other imposters
                    #else:
                        #continue #move on to the next imposter
                
                #if crewmate.get_tasks() == None and crewmate.get_dead() == False:
                    #if the crewmate is still alive and they've done all possible tasks,
                    #put them in the survivors list
                    #surviving_list.append(crewmate)
                    #crewmate_list.remove(crewmate)
                if crewmate_list == [] and len(dead_list) == (10 - len(self.__imposters)): 
                    print("Imposters have successfully eliminated all of the crewmates.")
                    print("Those that have survived: None")
                    print("Those that have perished: ", dead_list)
                    return False
                if self.__tasks == [] and len(surviving_list) > 0:
                    print("Crewmates have successfully completed all of their tasks.")
                    print("Those that have survived: ", surviving_list)
                    print("Those that have perished: ", dead_list)
                    return False
                if crewmate.get_dead() == False:
                    print("[Crewmate]:", crewmate, "is returning to cafeteria.")
                    cafeteria.enqueue(crewmate) #if the crewmate survives, they go back to the cafeteria
                #else:
                    #continue
                
    def journey(self):
        #responsible for each journey on the ship
        random_colors = self.assign_colors() #the list of the colors
        player_list = []
        #make a list to store each player in, for later convenience
        #create a crewmate for each of the ten players, give them a color,
        #and proceed to store them in the player list
        player1 = Crewmate()
        player2 = Crewmate()
        player3 = Crewmate()
        player4 = Crewmate()
        player5 = Crewmate()
        player6 = Crewmate()
        player7 = Crewmate()
        player8 = Crewmate()
        player9 = Crewmate()
        player10 = Crewmate()
        player_list.append(player1)
        player_list.append(player2)
        player_list.append(player3)
        player_list.append(player4)
        player_list.append(player5)
        player_list.append(player6)
        player_list.append(player7)
        player_list.append(player8)
        player_list.append(player9)
        player_list.append(player10)
        player1.set_color(random_colors[0])
        player2.set_color(random_colors[1])
        player3.set_color(random_colors[2])
        player4.set_color(random_colors[3])
        player5.set_color(random_colors[4])
        player6.set_color(random_colors[5])
        player7.set_color(random_colors[6])
        player8.set_color(random_colors[7])
        player9.set_color(random_colors[8])
        player10.set_color(random_colors[9])
        filename = input("What task file should the program read from? ")
        print("Deciding imposters...")
        print("Assigning tasks...")
        crewmate_list = self.assign_tasks(player_list, filename)
        #start the journey, where all of the crewmates are inside of the cafeteria
        self.core(crewmate_list)
        #core takes the game until the end, journey should be over by this comment

def main():
    #since i took care of everything i possibly could think of in both the helper functions for journey
    #and in the journey function itself, main will literally just call journey, which calls the helper
    #functions and pieces this whole mess together, hopefully.

    imported_ship = Ship()
    imported_ship.journey()




    #tl;dr please go easy on this one, I've tried everything I could think of.
if __name__ == "__main__":
    main()

#haha memory leaks go brrrrrr